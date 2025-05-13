from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Received webhook:", data)

    action = data.get("action")

    # Always close any open positions first
    print("Closing all open positions...")
    # Place Tradovate close command here

    if action == "buy":
        print("Placing long order...")
        # Place Tradovate long order here

    elif action == "sell":
        print("Placing short order...")
        # Place Tradovate short order here

    elif action == "close":
        print("Action was just 'close' – no new order placed.")

    else:
        print("Unknown action received.")

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
