from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Message: {message}")

    return redirect("/#contact")


if __name__ == "__main__":
    app.run(debug=True)