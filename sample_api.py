from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/data", methods=["GET", "POST"])
def get_data():
    return jsonify([
    {
        "campaign": "Brand_Exact_US",
        "type": "Brand",
        "impressions": 210000,
        "clicks": 12600,
        "ctr": "6.00%",
        "conversions": 756,
        "conv_rate": "6.00%",
        "cost": 8820,
        "cpc": 0.70
    },
    {
        "campaign": "Generic_Shoes_BMM",
        "type": "Generic",
        "impressions": 480000,
        "clicks": 9600,
        "ctr": "2.00%",
        "conversions": 480,
        "conv_rate": "5.00%",
        "cost": 14400,
        "cpc": 1.50
    },
    {
        "campaign": "Retargeting_CartAbandon",
        "type": "Retarget",
        "impressions": 95000,
        "clicks": 5700,
        "ctr": "6.00%",
        "conversions": 570,
        "conv_rate": "10.00%",
        "cost": 7410,
        "cpc": 1.30
    },
    {
        "campaign": "Competitor_Conquest",
        "type": "Competitor",
        "impressions": 198000,
        "clicks": 3960,
        "ctr": "2.00%",
        "conversions": 158,
        "conv_rate": "4.00%",
        "cost": 9900,
        "cpc": 2.50
    },
    {
        "campaign": "Brand_Broad_CA",
        "type": "Brand",
        "impressions": 145000,
        "clicks": 4350,
        "ctr": "3.00%",
        "conversions": 174,
        "conv_rate": "4.00%",
        "cost": 4350,
        "cpc": 1.00
    },
    {
        "campaign": "Generic_RunningShoes",
        "type": "Generic",
        "impressions": 115500,
        "clicks": 2310,
        "ctr": "2.00%",
        "conversions": 48,
        "conv_rate": "2.08%",
        "cost": 3440,
        "cpc": 1.49
    }
])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
