from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Received webhook:", data)

    action = data.get("action")

    # Step 1: Always close all open positions before taking any new action
    print("Closing all open positions...")
    # === Tradovate CLOSE ALL positions logic goes here ===

    # Step 2: Execute the intended new action AFTER everything is closed
    if action == "buy":
        print("Placing LONG order...")
        # === Tradovate LONG order logic goes here ===

    elif action == "sell":
        print("Placing SHORT order...")
        # === Tradovate SHORT order logic goes here ===

    elif action == "close":
        print("Received 'close' only – no new trade initiated.")

    else:
        print("Unknown action received.")

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
