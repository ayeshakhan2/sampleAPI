from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/data", methods=["GET", "POST"])
def get_data():
    return jsonify([
        {
            "campaign": "Search Campaign",
            "clicks": 200,
            "impressions": 8000,
            "cost": 500,
            "conversions": 25
        }
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
