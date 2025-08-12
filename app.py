from flask import Flask, request, redirect, url_for, send_from_directory
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)  # Enable CORS for all routes

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_TO = "var.reddy@gmail.com"

@app.route("/")
def home():
    # Serve index.html from root folder
    return send_from_directory('.', 'index.html')

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    try:
        msg = MIMEText(f"From: {name} <{email}>\n\n{message}")
        msg["Subject"] = "New RAPTTECH Contact Form Message"
        msg["From"] = EMAIL_USER
        msg["To"] = EMAIL_TO

        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtp.login(EMAIL_USER, EMAIL_PASS)
        smtp.send_message(msg)
        smtp.quit()

        return redirect(url_for("home"))
    except Exception as e:
        return f"Error: {e}"

# Optional: Serve any other static files (CSS, JS, images)
@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)

if __name__ == "__main__":
    app.run(debug=True)
