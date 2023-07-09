import subprocess
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    text = request.args.get("text", "figlet")
    p = subprocess.run(f"figlet '{text}'", shell=True, capture_output=True)
    output = p.stdout.decode("utf-8")

    return render_template("index.html", figlet=output)
