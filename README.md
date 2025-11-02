#ArogyaLink: The Digital Rosetta Stone for Indian Healthcare
Project Status: This project was successfully developed for the Smart India Hackathon 2025, solving Problem Statement #25026. We are proud to have been selected by our college, MIT Manipal to represent our college on national levels.

ArogyaLink is a lightweight, high-performance microservice that solves the critical interoperability gap between India's traditional Ayush terminologies (NAMASTE) and the modern, global WHO ICD-11 standard.

It acts as a real-time "translation bridge," allowing any Electronic Medical Record (EMR) system to support seamless "dual-coding" of diagnoses, unlocking value for patients, doctors, and national-level health analytics.

Our Approach: The "Glass Box" Expert Engine (Why We Beat AI)
This project tackles a high-stakes medical problem where trust and accuracy are more innovative than a "black box" guess.

While other approaches might use complex AI (like BioBERT) to predict mappings, this is fundamentally flawed:

The "Chicken-and-Egg" Flaw: AI needs a massive, pre-mapped dataset to learn from, but that dataset is the very thing this project is meant to create.

The "Trust" Flaw: In medicine, a statistical guess ("85% confident") is a liability. A doctor needs 100% certainty.

ArogyaLink is a transparent "glass box"—an Expert-Driven Rules Engine. We built the platform to capture and automate the application of expert medical knowledge, which is the correct, professional, and trustworthy solution.

Core Features
NAMASTE CSV Ingestion: Uses Pandas to load and process the 2,900+ official NAMASTE terms at startup.

Live WHO API Integration: Securely connects to the official WHO ICD-11 API using OAuth 2.0 to fetch live, up-to-date medical data.

Expert-Driven Mapping: Uses a prototype FHIR ConceptMap (mappings.json) to store and serve expert-defined, 100% accurate translations.

Intelligent Fuzzy Search: Includes an intelligent search endpoint that can handle user typos (e.g., jvarh is correctly identified as jvaraH).

Interactive Web UI: A simple, clean frontend built with HTML/JS to demonstrate the complete, end-to-end functionality of the service.

Lightweight & Fast: Built with FastAPI for high-performance, asynchronous requests.

Technology Stack
Backend: Python 3, FastAPI, Uvicorn

Data: Pandas (for CSV ingestion)

API Integration: requests (for WHO API)

Search Logic: thefuzz (for fuzzy string matching)

Frontend: HTML5, CSS3, Vanilla JavaScript

Security: python-dotenv (for API key management)

🚀 How to Run This Project
Follow these steps to get your local development environment set up and running.

1. Clone the Repository
Bash

git clone https://github.com/your-username/ArogyaLink.git
cd ArogyaLink
2. Create and Activate a Virtual Environment
Bash

# Create the environment
python3 -m venv venv

# Activate the environment
source venv/bin/activate
3. Install Dependencies
This project uses several Python packages. (Note: python-Levenshtein is recommended for thefuzz to run much faster).

Bash

pip install fastapi "uvicorn[standard]" requests python-dotenv pandas jinja2 thefuzz python-Levenshtein
4. Create Your Environment File
Create a file named .env in the root of the project directory. This is crucial for securely storing your API keys.

# .env file

WHO_CLIENT_ID="your_who_client_id_goes_here"
WHO_CLIENT_SECRET="your_who_client_secret_goes_here"
5. Add Your Data Files
Place the following files (which are not in this repo) into the root ArogyaLink directory:

namaste_data.csv (The official NAMASTE terminology CSV, renamed)

mappings.json (Your prototype FHIR ConceptMap)

6. Run the Server
You're all set! Use Uvicorn to run the FastAPI server.

Bash

uvicorn main:app --reload
7. View the Prototype
Open your web browser and navigate to: http://127.0.0.1:8000

You can now use the fully functional prototype!
