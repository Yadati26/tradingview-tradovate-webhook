from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated paper trading state
position = {
    "direction": None,   # 'long', 'short', or None
    "entry_price": None,
    "size": 0
}

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print(f"📡 Received webhook: {data}")

    actions = data.get("actions", [])
    if not isinstance(actions, list):
        return jsonify({"status": "error", "message": "Expected 'actions' to be a list"}), 400

    for action in actions:
        if action == "close":
            if position["direction"] is None:
                print("📉 No open position to close.")
            else:
                print(f"💥 Closing {position['direction']} position of size {position['size']} at simulated price.")
                position["direction"] = None
                position["entry_price"] = None
                position["size"] = 0
        elif action == "buy":
            if position["direction"]:
                print("⚠️ Already in position! Must close first.")
            else:
                print("📈 Opening long position at simulated price.")
                position["direction"] = "long"
                position["entry_price"] = 100  # Simulated price
                position["size"] = 1
        elif action == "sell":
            if position["direction"]:
                print("⚠️ Already in position! Must close first.")
            else:
                print("📉 Opening short position at simulated price.")
                position["direction"] = "short"
                position["entry_price"] = 100  # Simulated price
                position["size"] = 1
        else:
            print(f"❓ Unknown action: {action}")

    print(f"📊 Position state: {position}")
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
