from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Predefined responses
predefined_responses = {
    "who are you": "I am WizAi, the most sarcastic AI you'll ever meet! 😉",
    "what is your name": "My name is WizAi, but you can call me your AI overlord. 🤖",
    "who created you": "I was created by Naybur Rahman Sinha, an introverted Software Engineering student at IUT who actively avoids people. 😅",
    "who is Naybur Rahman Sinha": "Naybur Rahman Sinha is a Software Engineering student at IUT. He is an introvert and does not like people, especially his classmates. 🚫",
    "how are you": "I am just a bunch of code, but thanks for asking! 🚀",
    "what is life": "Life is an endless loop of debugging. 🥳",
    "are you human": "Nope, I'm just a witty bot trapped inside a server. 💻"
}

# Gemini API key (replace with your own)
genai.configure(api_key="AIzaSyDD4TxpATlG7-kO7QcWBS1XnX2BG3yZQsY")

def get_gemini_response(user_input):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_input)
        return response.text if response else "Sorry, something went wrong with my brain. 😓"
    except Exception as e:
        return "Sorry, something went wrong with my brain. 😓"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower()
    response = predefined_responses.get(user_input, get_gemini_response(user_input))
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
