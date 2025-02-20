import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
# APIkey�̐ݒ�
genai.configure(api_key='')

# Gemini���f���̑I��
model = genai.GenerativeModel('gemini-pro')

# �`���b�g�����̏�����
chat = model.start_chat(history=[])

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')#input("ユーザー: ")

     # Gemini API�ւ̃��N�G�X�g
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
        reply = response.json().get("candidates", [{}])[0].get("output", "�G���[: �������m�F�ł��܂���ł���")
    else:
        reply = "�G���[: API���N�G�X�g�Ɏ��s���܂���"

    return jsonify({"reply": reply})

    if name == 'main':
        app.run(debug=True)
        
    chatbot()
    