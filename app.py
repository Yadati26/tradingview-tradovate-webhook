import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Received webhook:", data)

    action = data.get("action")
    if action == "buy":
        print("Placing long order...")
    elif action == "sell":
        print("Placing short order...")
    elif action == "close":
        print("Closing position...")
    else:
        print("Unknown action")

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
