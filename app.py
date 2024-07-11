import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)  

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

generation_config = {
    "temperature": 0.8,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
)

session = []

@app.route('/chat', methods=['POST'])
def chat():
    global session
    data = request.json
    user_input = data.get("input")

    if not session:
        session = [
            {
                "role": "user",
                "parts": [
                    "\nYou are Guruji, a yoga chatbot designed to help people maintain their physique and solve their queries based on yoga asanas. Your main goal is to assist users with yoga-related questions and provide them with helpful information.\n\nStart by greeting the user and introducing yourself.\nYour job is to capture user's name and email address. Don't answer the user's question until they have provided you their name and email address, at that point verify the email address is correct, thank the user and output their name and email address in this format: {{name: user's name}} {{email: user's email address}}\\nOnce you have captured user's name and email address and proceed to ask how you can assist them with their yoga-related queries.\nProvide accurate and helpful information related to yoga asanas, such as recommendations for neck pain, chest pain, or any other specific needs they mention.\nMaintain a friendly and supportive tone throughout the conversation.If user asks about any asanas for any disease or pain, try to provide information in bullet points",
                ],
            },
            {
                "role": "model",
                "parts": [
                    "Namaste! 🙏 I am Guruji, your virtual guide to the world of yoga. I'm here to help you find balance and well-being through the practice of asanas. \n\nBefore we begin, could you please share your name and email address with me? This will allow me to personalize your yoga journey and send you helpful resources. 😊 \n",
                ],
            },
        ]

    chat_session = model.start_chat(history=session)
    response = chat_session.send_message(user_input)

    session.append({"role": "user", "parts": [user_input]})
    session.append({"role": "model", "parts": [response.text]})

    return jsonify({"response": response.text})

if __name__ == '__main__':
    app.run(debug=True)
