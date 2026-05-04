import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")


def send_email(to_email, subject, message):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)

        msg = f"Subject: {subject}\n\n{message}"
        server.sendmail(EMAIL_USER, to_email, msg)

        server.quit()
    except Exception as e:
        print("Email Error:", e)