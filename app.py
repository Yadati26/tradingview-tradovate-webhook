@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Received webhook:", data)

    actions = data.get("actions", [])
    if not isinstance(actions, list):
        return jsonify({"status": "error", "message": "Expected 'actions' to be a list"}), 400

    for action in actions:
        if action == "buy":
            print("Placing long order...")
            # Place long via Tradovate API
        elif action == "sell":
            print("Placing short order...")
            # Place short via Tradovate API
        elif action == "close":
            print("Closing all positions...")
            # Flatten all positions via Tradovate API
        else:
            print(f"Unknown action: {action}")

    return jsonify({"status": "ok"})
