import PyPDF2
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load job description
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "..", "job_description.txt")

with open(file_path, "r", encoding="utf-8") as f:
    job_desc = f.read()


def extract_text(file):
    pdf = PyPDF2.PdfReader(file.file)
    text = ""
    for page in pdf.pages:
        if page.extract_text():
            text += page.extract_text()
    return text


async def calculate_score(file):
    resume_text = extract_text(file)

    text_data = [resume_text, job_desc]

    cv = CountVectorizer().fit_transform(text_data)
    score = cosine_similarity(cv)[0][1]

    return round(score * 100, 2)