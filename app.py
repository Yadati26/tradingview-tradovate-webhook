from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Received webhook:", data)

    actions = data.get("actions", [])
    for action in actions:
        if action == "buy":
            print("Opening long...")
        elif action == "sell":
            print("Opening short...")
        elif action == "close":
            print("Closing position...")
        else:
            print("Unknown action:", action)

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
