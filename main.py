from fastapi import FastAPI, HTTPException, Depends, status, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List, Optional, Dict
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv
import time
import pandas as pd
import json

load_dotenv()

WHO_CLIENT_ID = os.getenv("WHO_CLIENT_ID")
WHO_CLIENT_SECRET = os.getenv("WHO_CLIENT_SECRET")
WHO_AUTH_URL = "https://icdaccessmanagement.who.int/connect/token"
WHO_API_ENTITY_URL_BASE = "https://id.who.int/icd/entity"

app = FastAPI(title="ArogyaLink Full Integration Demo")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static")

NAMASTE_DATA_STORE: Dict[str, Dict] = {}
ICD11_MAPPINGS_LOWER: Dict[str, str] = {} # For case-insensitive lookup

class DualCodeResponse(BaseModel):
    namaste_term: str
    namaste_code: str
    icd11_title: str
    icd11_code: str
    icd11_definition: Optional[str] = None

_who_api_token_cache = {"token": None, "expiry": 0}

async def get_who_api_auth_token():
    current_time = time.time()
    if _who_api_token_cache["token"] and _who_api_token_cache["expiry"] > current_time:
        return _who_api_token_cache["token"]
    if not WHO_CLIENT_ID or not WHO_CLIENT_SECRET:
        raise HTTPException(status_code=500, detail="WHO API credentials not set.")
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"grant_type": "client_credentials", "client_id": WHO_CLIENT_ID, "client_secret": WHO_CLIENT_SECRET, "scope": "icdapi_access"}
    try:
        response = requests.post(WHO_AUTH_URL, headers=headers, data=data)
        response.raise_for_status()
        token_data = response.json()
        token = token_data["access_token"]
        expires_in = token_data.get("expires_in", 3600)
        _who_api_token_cache["token"] = token
        _who_api_token_cache["expiry"] = current_time + expires_in - 60
        return token
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Failed to get WHO API token: {e}")

@app.on_event("startup")
async def load_data():
    global NAMASTE_DATA_STORE, ICD11_MAPPINGS_LOWER
    
    csv_file_path = "namaste_data.csv"
    try:
        df = pd.read_csv(csv_file_path)
        required_cols = ['NAMC_term', 'NAMC_CODE']
        if not all(col in df.columns for col in required_cols):
            raise ValueError(f"CSV must contain columns: {required_cols}")
        
        df_clean = df[required_cols].dropna().drop_duplicates(subset=['NAMC_term']).set_index('NAMC_term')
        NAMASTE_DATA_STORE = df_clean.to_dict(orient='index')
        print(f"Loaded {len(NAMASTE_DATA_STORE)} unique NAMASTE entries from {csv_file_path}")
    except Exception as e:
        print(f"ERROR: Failed to load '{csv_file_path}': {e}")
        NAMASTE_DATA_STORE = {}

    mappings_file_path = "fhir_concept_map.json"
    try:
        with open(mappings_file_path, 'r') as f:
            mappings = json.load(f)
            ICD11_MAPPINGS_LOWER = {k.lower(): v for k, v in mappings.items()}
        print(f"Loaded {len(ICD11_MAPPINGS_LOWER)} ICD-11 mappings from {mappings_file_path}")
    except Exception as e:
        print(f"ERROR: Failed to load '{mappings_file_path}': {e}")
        ICD11_MAPPINGS_LOWER = {}

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/map-namaste/{search_term}", response_model=DualCodeResponse)
async def map_namaste_to_icd11(search_term: str, token: str = Depends(get_who_api_auth_token)):
    if not NAMASTE_DATA_STORE or not ICD11_MAPPINGS_LOWER:
        raise HTTPException(status_code=503, detail="Server data not loaded. Check logs.")

    # *** THIS IS THE CHANGED LOGIC FOR EXACT MATCH ***
    search_term_lower = search_term.lower()
    matched_term = next((term for term in NAMASTE_DATA_STORE if term.lower() == search_term_lower), None)

    if not matched_term:
        raise HTTPException(status_code=404, detail=f"NAMASTE term '{search_term}' not found.")

    icd11_full_uri = ICD11_MAPPINGS_LOWER.get(matched_term.lower())

    if not icd11_full_uri:
        raise HTTPException(status_code=404, detail=f"ICD-11 mapping not available for '{matched_term}' in this demo.")
        
    icd11_id = icd11_full_uri.split('/')[-1]
    
    headers = {"Authorization": f"Bearer {token}", "Accept-Language": "en", "API-Version": "v2"}
    try:
        response = requests.get(f"{WHO_API_ENTITY_URL_BASE}/{icd11_id}", headers=headers)
        response.raise_for_status()
        data = response.json()
        
        icd11_title = data.get("title", {}).get("@value", "No Title Available")
        icd11_definition = data.get("definition", {}).get("@value")
        
        namaste_details = NAMASTE_DATA_STORE[matched_term]
        
        return DualCodeResponse(
            namaste_term=matched_term,
            namaste_code=namaste_details['NAMC_CODE'],
            icd11_title=icd11_title,
            icd11_code=icd11_id,
            icd11_definition=icd11_definition
        )
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Failed to fetch live ICD-11 details from WHO API: {e}")