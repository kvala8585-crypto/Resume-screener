from fastapi import FastAPI, UploadFile, File, Form
from app.ai_engine import calculate_score
from app.email_service import send_email

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Resume Screener API Running 🚀"}


@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    score = await calculate_score(file)
    return {"filename": file.filename, "score": score}


@app.post("/send-email")
def email_api(to_email: str = Form(...), candidate_name: str = Form(...)):
    send_email(
        to_email,
        "Job Selection",
        f"Congratulations {candidate_name}, you are shortlisted!"
    )
    return {"status": "Email sent"}