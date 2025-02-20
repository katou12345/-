import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)

# APIkeyの設定
genai.configure(api_key=os.getenv("API_KEY"))


# Geminiモデルの選択
model = genai.GenerativeModel('Gemini 2.0 Flash')#gemini-pro

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_route():
    user_input = request.json.get('message')

    if not user_input:
        return jsonify({"reply": "エラー: 入力が必要です"})

    # Gemini APIへのリクエスト
    try:
        response = model.generate_content(user_input)
        reply = response.text
    except Exception as e:
        reply = f"エラー: {str(e)}"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
   
