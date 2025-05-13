@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Received webhook:", data)

    actions = data.get("actions", [])
    if not isinstance(actions, list):
        return jsonify({"status": "error", "message": "Expected 'actions' to be a list"}), 400

    position_state = "flat"

    for action in actions:
        if action == "buy":
            if position_state == "short":
                print("Closing short before going long...")
                # Close short via Tradovate
                position_state = "flat"
            print("Opening long...")
            # Place long via Tradovate
            position_state = "long"

        elif action == "sell":
            if position_state == "long":
                print("Closing long before going short...")
                # Close long via Tradovate
                position_state = "flat"
            print("Opening short...")
            # Place short via Tradovate
            position_state = "short"

        elif action == "close":
            if position_state == "long":
                print("Closing long...")
            elif position_state == "short":
                print("Closing short...")
            else:
                print("Nothing to close.")
            position_state = "flat"

        else:
            print(f"Unknown action: {action}")

    return jsonify({"status": "ok"})
