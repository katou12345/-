import google.generativeai as genai

# APIキーの設定
genai.configure(api_key='apikey')

# Geminiモデルの選択
model = genai.GenerativeModel('gemini-pro')

# チャット履歴の初期化
chat = model.start_chat(history=[])

# チャットボットのメインループ
def chatbot():
    print("\nGemini Chatbotへようこそ！\n'終了'と入力するとチャットを終了します。\n")
    while True:
        user_input = input("ユーザー: ")
        if user_input.lower() in ['終了', 'exit', 'quit']:
            print("Gemini Chatbotを終了します。さようなら！")
            break

        # ユーザーの入力に基づいて応答を生成
        response = chat.send_message(user_input)

        # チャットボットの応答を表示
        print(f"Gemini: {response.text}")

if __name__ == "__main__":
    chatbot()