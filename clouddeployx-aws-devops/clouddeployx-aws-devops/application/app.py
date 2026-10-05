from flask import Flask, jsonify
import os

app = Flask(__name__)
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

@app.get("/")
def home():
    return jsonify({
        "application": "CloudDeployX",
        "message": "CloudDeployX is running on AWS EKS!",
        "version": APP_VERSION,
        "status": "healthy"
    })

@app.get("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.get("/ready")
def ready():
    return jsonify({"status": "ready"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
