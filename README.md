# AI Resume Screening & Automation System

An end-to-end AI-powered system that automates resume screening, candidate ranking, and email notifications.
Built using FastAPI for backend APIs and Streamlit for user interaction, and deployed on Render.


##  Key Features

*  Upload and parse multiple PDF resumes
*  Match resumes with job descriptions using NLP
*  Rank candidates based on similarity score
*  REST API support using FastAPI
*  Automated email notification system
*  Deployed and accessible via public API endpoints
  
## System Architecture

Frontend (Streamlit UI)
⬇
Backend API (FastAPI + Uvicorn)
⬇
AI Engine (Cosine Similarity - NLP)
⬇
Email Service (SMTP)


##  API Endpoints

* **POST /upload-resume** → Upload resume and get similarity score
* **POST /send-email** → Send selection email to candidate

Example Deployment:

* `/upload-resume`
* `/send-email`

## Tech Stack

* Python
* FastAPI (Backend APIs)
* Uvicorn (Server)
* Streamlit (Frontend UI)
* Scikit-learn (NLP similarity)
* PyPDF2 (PDF parsing)
* Python-dotenv (Environment variables)
* SMTP (Email automation)

---

## Project Structure

```
AI_Resume_Screener/
│
├── app/
│   ├── main.py
│   ├── ai_engine.py
│   ├── email_service.py
│
├── app.py (Streamlit UI)
├── job_description.txt
├── requirements.txt
├── 
└── README.md
```

##  Installation & Setup

```bash
git clone <https://github.com/kvala8585-crypto/Resume-screener/>
cd AI_Resume_Screener

pip install -r requirements.txt
python -m spacy download en_core_web_sm


### Run Streamlit UI

```bash
streamlit run app.py


### Run FastAPI Server

```bash
uvicorn app.main:app --reload

---

##  How It Works

1. Upload resume(s) via UI or API
2. System extracts text from PDF
3. Compares with job description using NLP
4. Generates similarity score
5. Ranks candidates
6. Sends email to selected candidate



##  Security Notes


---

##  Future Improvements

* Semantic matching using Transformer models (BERT / LLMs)
* Database integration (PostgreSQL / MongoDB)
* Automated workflows using n8n / Zapier
* Multi-job role support
* Admin dashboard for recruiters

---

## 👨‍💻 Author

Kavi Vala
