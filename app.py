from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("✅ Received webhook:", data)

    actions = data.get("actions", [])
    if not isinstance(actions, list):
        return jsonify({"status": "error", "message": "Expected 'actions' to be a list"}), 400

    for action in actions:
        print("📍 Closing all open positions...")

        if action == "buy":
            print("➡️ Opening long position...")

        elif action == "sell":
            print("➡️ Opening short position...")

        elif action == "close":
            print("✅ Just closing position...")

        else:
            print(f"❗ Unknown action: {action}")

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1000)
