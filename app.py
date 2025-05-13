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
