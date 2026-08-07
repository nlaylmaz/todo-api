from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "tasks": [
            "Docker ogren",
            "CI/CD ogren"
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

