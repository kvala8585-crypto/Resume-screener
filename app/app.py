import smtplib
import streamlit as st
import os
import PyPDF2
import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()

# ✅ Get email credentials from .env
from_email = os.getenv("EMAIL_USER")
password = os.getenv("EMAIL_PASS")


def send_email(to_email, subject, message):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_email, password)

        msg = f"Subject: {subject}\n\n{message}"
        server.sendmail(from_email, to_email, msg)

        server.quit()
        return True
    except Exception as e:
        st.error(f"Email Error: {e}")
        return False


# ✅ Load NLP model
nlp = spacy.load("en_core_web_sm")


# ✅ Function to extract text from PDF
def extract_text_from_pdf(file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(file)
    for page in pdf_reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text


# ✅ FIX: Dynamic path for job_description.txt
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "job_description.txt")

try:
    with open(file_path, "r", encoding="utf-8") as f:
        job_desc = f.read()
except FileNotFoundError:
    st.error("❌ job_description.txt file not found. Please keep it in same folder as app.py")
    st.stop()


st.title("AI Resume Screening System 🚀")

uploaded_files = st.file_uploader("Upload Resumes (PDF)", accept_multiple_files=True)

top_candidate = None  # ✅ important fix

if uploaded_files:
    scores = []

    for file in uploaded_files:
        resume_text = extract_text_from_pdf(file)

        text_data = [resume_text, job_desc]

        cv = CountVectorizer().fit_transform(text_data)
        similarity = cosine_similarity(cv)[0][1]

        scores.append((file.name, similarity))

    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    top_candidate = scores[0][0]

    st.subheader("📊 Ranking of Candidates")

    for name, score in scores:
        st.write(f"{name} → Score: {round(score*100,2)}%")

    st.success(f"Top Candidate Selected: {top_candidate}")


# ✅ Email input
email = st.text_input("Enter Candidate Email")

# ✅ Send Email
if st.button("Send Email"):
    if not email:
        st.warning("⚠️ Please enter email")
    elif not top_candidate:
        st.warning("⚠️ Please upload resumes first")
    else:
        success = send_email(
            email,
            "Job Selection",
            f"Congratulations {top_candidate}, you are shortlisted!"
        )
        if success:
            st.success("Email Sent Successfully ✅")