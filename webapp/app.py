import os
import sys
import zipfile
import smtplib
from email.message import EmailMessage
from flask import Flask, render_template, request

# Allow importing mashup_core
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from mashup_core import clear_folders, download_videos, cut_audios, merge_audios

app = Flask(__name__)

# 🔐 Replace with your Gmail + App Password
SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
APP_PASSWORD = os.environ.get("APP_PASSWORD")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    singer = request.form["singer"]
    num_videos = int(request.form["videos"])
    duration = int(request.form["duration"])
    receiver_email = request.form["email"]

    try:
        # Step 1: Generate Mashup
        clear_folders()
        download_videos(singer, num_videos)
        mp3_files = cut_audios(duration)
        merge_audios(mp3_files, "mashup.mp3")

        # Step 2: Zip file
        mp3_path = os.path.join("cli", "final_output", "mashup.mp3")
        zip_path = os.path.join("cli", "final_output", "mashup.zip")

        with zipfile.ZipFile(zip_path, "w") as zipf:
            zipf.write(mp3_path, arcname="mashup.mp3")

        # Step 3: Send Email
        send_email(receiver_email, zip_path)

        return "Mashup created and sent to your email successfully!"

    except Exception as e:
        return f"Error occurred: {str(e)}"


def send_email(receiver_email, attachment_path):
    msg = EmailMessage()
    msg["Subject"] = "Your Mashup File"
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email
    msg.set_content("Your mashup file is attached. Enjoy!")

    with open(attachment_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="zip",
            filename="mashup.zip"
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)


if __name__ == "__main__":
    app.run(debug=True)
