# 🤖 AI Resume Screening System

This is an AI-powered Resume Screening Web App built using Streamlit.  
It helps recruiters automatically rank resumes based on a job description.

---

## 🚀 Features

- Upload multiple resumes (PDF)
- Extracts text from resumes
- Compares resumes with job description
- Ranks candidates using cosine similarity
- Selects top candidate automatically
- Send selection email to candidate

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Scikit-learn
- SpaCy
- PyPDF2
- SMTP (Email sending)

---

## 📂 Project Structure
AI_Resume_Screener/
│── app.py
│── job_description.txt
│── requirements.txt
│── README.md

---

## ⚙️ Installation

```bash
git clone <your-repo-link>
cd AI_Resume_Screener
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py

📌 Usage

Upload resumes (PDF)
System will rank candidates
Top candidate will be selected automatically
Enter candidate email
Click "Send Email"

⚠️ Important Notes

Do NOT hardcode email/password in production
Use environment variables instead
Gmail requires App Password (not real password)

🔮 Future Improvements

AI-based semantic matching (BERT / LLM)
Database integration (store resumes)
Dashboard for HR analytics
API integration (n8n / Zapier automation)
Multi-job role support

👨‍💻 Author

Kavi Vala