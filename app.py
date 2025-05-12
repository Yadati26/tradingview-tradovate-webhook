from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Received webhook:", data)

    # Basic logic
    action = data.get("action")
    if action == "buy":
        print("Placing long order...")
        # Call Tradovate API here
    elif action == "sell":
        print("Placing short order...")
        # Call Tradovate API here
    elif action == "close":
        print("Closing position...")
        # Call Tradovate API here
    else:
        print("Unknown action")

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
