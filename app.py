from flask import Flask, render_template, request, redirect, url_for, make_response
from os import makedirs, path
import functions

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    uploaded_file = request.files["file"]
    text = request.form["text"]
    makedirs("uploads", exist_ok=True)

    if uploaded_file.filename != "":
        filepath = path.join("uploads", uploaded_file.filename)
        uploaded_file.save(filepath)
        response_text = functions.convert(filepath)
        # response = make_response(response_text, 200)
        # response.mimetype = "text/plain"
    else:
        response_text = functions.convert_text(text)
        # response = make_response(response_text, 200)
        # response.mimetype = "text/plain"
    # return response #redirect(url_for('index'))
    return render_template("index.html", text=response_text)


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(host="0.0.0.0", port=8000)
