# ArogyaLink: The Digital Rosetta Stone for Indian Healthcare


[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

> 🎉 **Project Status:** We are incredibly proud to announce that ArogyaLink was successfully developed for the Smart India Hackathon 2025, solving **Problem Statement \#25026**, and has been **selected by college, MIT Manipal to represent our college at national level.\!**

---

## 💡 The Problem: Two Worlds, Disconnected

India's healthcare system uniquely operates with two powerful, yet digitally disconnected, languages:

1.  **Traditional Medicine (NAMASTE):** The rich, detailed terminology for Ayush.
2.  **Global Modern Medicine (WHO ICD-11):** The universal standard for diagnostics, statistics, and billing.

This digital chasm creates a critical interoperability gap, leading to:

* ❌ **Compromised Patient Safety:** Fragmented health records, leading to potential misdiagnosis or unsuitable treatment when patient history from one system is unintelligible to the other.
* 💰 **Economic Friction:** Delays and rejections in insurance claims for Ayush treatments due to non-standardized codes.
* 📊 **Policy Blindness:** Inability for the Ministry of Ayush and other government bodies to conduct unified, evidence-based national health analytics.

## 🎯 Our Solution: ArogyaLink - The Digital Rosetta Stone

ArogyaLink is a lightweight, high-performance microservice designed to be the **definitive, real-time translation bridge** between NAMASTE and ICD-11. It's built to integrate seamlessly into existing Electronic Medical Record (EMR) systems, enabling crucial "dual-coding" of diagnoses.

## ✨ Why ArogyaLink is the Winning Solution (The "Glass Box" Advantage)

In high-stakes medical applications, **trust and 100% accuracy are paramount.** Our approach stands in stark contrast to speculative methods:

* **🚫 Not an AI 'Black Box':** We deliberately avoid using AI (e.g., BioBERT for semantic matching) for core mapping. Why?
    1.  **The "Chicken-and-Egg" Flaw:** AI needs a massive, pre-mapped, expert-validated dataset to learn from, but that dataset is the very thing this project aims to create.
    2.  **The "Trust" Flaw:** AI provides probabilistic guesses ('85% confident'). In medicine, a statistical guess is a liability; doctors need certainty.
* ✅ **The "Glass Box" Expert Engine:** ArogyaLink is a transparent, **Expert-Driven Rules Engine**. We provide the robust platform to capture and automate the application of *expert-validated* medical knowledge. This is the **correct, professional, and trustworthy solution** for a national health initiative.

## 🛠️ Core Features

* **NAMASTE CSV Ingestion:** Efficiently loads and processes the ~2,900 official NAMASTE terms from a CSV into memory for lightning-fast lookups using Pandas.
* **Live WHO API Integration:** Securely connects to the official WHO ICD-11 API (via OAuth 2.0) to fetch live, up-to-date, and globally recognized medical entity details.
* **Expert-Driven Mapping (FHIR ConceptMap):** Utilizes a prototype `FHIR ConceptMap` (`mappings.json`) to store and serve 100% accurate, expert-defined translations.
* **Intelligent Fuzzy Search:** Includes robust fuzzy string matching (`thefuzz`) to gracefully handle common user typos (e.g., `jvarh` correctly identifies `jvaraH`).
* **Interactive Web UI:** A clean, intuitive frontend (HTML/CSS/JS) to demonstrate the complete, end-to-end functionality in a user-friendly manner.
* **Lightweight & Fast:** Built with **FastAPI** for high-performance, asynchronous request handling, ensuring scalability and responsiveness.
* **FHIR R4 Compliant:** Designed with interoperability standards like FHIR R4 to ensure future scalability and integration.

## 🚀 Impact & Benefits

ArogyaLink is more than just a translator; it's a foundational component for a digitally integrated Indian healthcare system:

* 🩺 **For Clinicians:** An efficient, error-reducing workflow, saving valuable time and improving diagnostic accuracy.
* 🩹 **For Patients:** Complete, holistic, and portable digital health records, ensuring safer and more informed care.
* 🏥 **For Hospitals & EMRs:** Seamless compliance with India's 2016 EHR Standards and ABHA-linked security integration.
* 💲 **For Insurers:** Standardized codes for rapid and transparent Ayush claims processing.
* 🇮🇳 **For Ministry of Ayush:** The foundation for accurate, real-time national morbidity reporting and evidence-based policy formulation.

## ⚙️ Technology Stack

* **Backend:** Python 3, FastAPI, Uvicorn
* **Data Processing:** Pandas
* **API Integration:** `requests`
* **Fuzzy Search:** `thefuzz` (with `python-Levenshtein` for speed)
* **Environment Management:** `python-dotenv`
* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **Templating:** Jinja2

---

## 🏃 Getting Started: Run ArogyaLink Locally

Follow these steps to set up and run the ArogyaLink prototype on your local machine.

### 1. Clone the Repository

```bash
git clone [https://github.com/your-github-username/ArogyaLink.git](https://github.com/your-github-username/ArogyaLink.git)
cd ArogyaLink
