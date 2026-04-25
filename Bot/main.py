import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    msg = data.get("message", "")

    # simple replies
    if "hello" in msg.lower():
        reply = "Hello from bot 😎"
    elif "players" in msg.lower():
        reply = "Server is active 🔥"
    else:
        reply = "I am a bot 🤖"

    return {"reply": reply}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
