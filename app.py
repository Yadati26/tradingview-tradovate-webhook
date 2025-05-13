@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Received webhook:", data)

    actions = data.get("actions", [])
    if not isinstance(actions, list):
        return jsonify({"status": "error", "message": "Expected 'actions' to be a list"}), 400

    for action in actions:
        print("Closing all open positions...")
        if action == "buy":
            print("Placing LONG order...")
        elif action == "sell":
            print("Placing SHORT order...")
        elif action == "close":
            print("Only closing...")
        else:
            print(f"Unknown action: {action}")

    return jsonify({"status": "ok"})
