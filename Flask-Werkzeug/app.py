from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World via flask and WerkZeug"



if __name__ == "__main__":
    app.run(port=5000, debug=True, host="0.0.0.0")