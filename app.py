from flask import Flask, render_template, request, redirect
import csv
import os
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        file_exists = os.path.isfile("messages.csv")

        with open("messages.csv", "a", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            if not file_exists:
                writer.writerow([
                    "Date",
                    "Name",
                    "Email",
                    "Subject",
                    "Message"
                ])

            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                name,
                email,
                subject,
                message
            ])

        return redirect("/contact")

    return render_template("contact.html")


@app.route("/messages")
def messages():

    contact_messages = []

    if os.path.isfile("messages.csv"):

        with open("messages.csv", "r", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for row in reader:
                contact_messages.append(row)

    return render_template(
        "messages.html",
        messages=contact_messages
    )


if __name__ == "__main__":
    app.run(debug=True)