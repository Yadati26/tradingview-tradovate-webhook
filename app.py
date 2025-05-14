from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("✅ Received webhook:", data)

    actions = data.get("actions", [])
    if not isinstance(actions, list):
        print("❌ Invalid format. 'actions' must be a list.")
        return jsonify({"status": "error", "message": "Expected 'actions' to be a list"}), 400

    for action in actions:
        if action == "close":
            print("📍 Closing all open positions...")
            # TODO: Replace with actual Tradovate API call to close all positions
            print("✅ Just closing position...")

        elif action == "buy":
            print("📍 Closing all open positions before long...")
            # TODO: Replace with actual Tradovate API call to close positions
            print("🟢 Opening long position...")
            # TODO: Replace with Tradovate API call to open long position

        elif action == "sell":
            print("📍 Closing all open positions before short...")
            # TODO: Replace with actual Tradovate API call to close positions
            print("🔴 Opening short position...")
            # TODO: Replace with Tradovate API call to open short position

        else:
            print(f"⚠️ Unknown action: {action}")

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
