import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
# APIkeyの設定
genai.configure(api_key='')

# Geminiモデルの選択
model = genai.GenerativeModel('gemini-pro')

# チャット履歴の初期化
chat = model.start_chat(history=[])

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')#input("繝ｦ繝ｼ繧ｶ繝ｼ: ")

     # Gemini APIへのリクエスト
    headers = {"Content-Type": "application/json"}
    payload = {
        "prompt": {"text": user_input},
        "temperature": 0.7
    }
    
    response = requests.post(

        json=payload,
        headers=headers
    )

    if response.status_code == 200:
        reply = response.json().get("candidates", [{}])[0].get("output", "エラー: 応答が確認できませんでした")
    else:
        reply = "エラー: APIリクエストに失敗しました"

    return jsonify({"reply": reply})

    if name == 'main':
        app.run(debug=True)
        
    chatbot()
    