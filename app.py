from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
from urllib.parse import urlencode

# Load environment variables from .env file
load_dotenv()

# app = Flask(__name__, static_folder='.', static_url_path='')


# Tell Flask: templates and static files are in the root directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(
    __name__,
    template_folder=BASE_DIR,   # point templates to root
    static_folder=BASE_DIR      # point static files to root
)
CORS(app)  # Enable CORS for all routes

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_TO = os.getenv("EMAIL_TO")

# this code belos is to not use the cache 
@app.after_request
def add_header(response):
    response.cache_control.no_cache = True
    response.cache_control.no_store = True
    response.cache_control.must_revalidate = True
    return response

#---------------------------------

#@app.route("/")
@app.route("/")
def home():
    # Serve index.html from root folder
    # return send_from_directory('.', 'index.html')
    return render_template("/index.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    # print(f"USER: '{EMAIL_USER}'")
    # print(f"PASS LENGTH: {EMAIL_PASS}")
    # print(f"EMAIL TO: {email}")
    
    # Same email logic as before...
    try:
        msg = MIMEText(f"From: {name} <{email}>\n\n{message}")
        msg["Subject"] = "New RAPTTECH Contact Form Message"
        msg["From"] = EMAIL_USER
        msg["To"] = email

        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtp.login(EMAIL_USER, EMAIL_PASS)
        smtp.send_message(msg)
        smtp.quit()

        # Redirect to home with success message
         # ✅ Redirect with success query parameter
        # return redirect(url_for("home", success="true"))'
        return redirect("/?success=true")

    except Exception as e:
        # ✅ Redirect with failure query parameter
        # return redirect(url_for("home", success="false"))
        return redirect("/?success=false")

# Optional: Serve any other static files (CSS, JS, images)
@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)

if __name__ == "__main__":
    app.run(debug=True)
