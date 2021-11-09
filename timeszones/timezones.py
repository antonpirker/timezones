from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return jsonify({"timezones": f"{request.base_url}timezones"})


@app.route("/timezones", methods=["GET"])
def timezones():
    return jsonify({"hello": f"world"})
