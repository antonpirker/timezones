from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return jsonify({"hello": f"world"})


@app.route("/timezones", methods=["GET"])
def timezones():
    return jsonify({"hello": f"world"})
