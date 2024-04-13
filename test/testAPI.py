import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def query_all():
    return jsonify([{"id": 1, "text": "hello world!"}, {"id": 2, "text": "goodbye world!"}])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000) # host="0.0.0.0" makes Flask app accessible from external hosts