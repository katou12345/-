document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("chatForm").addEventListener("submit", sendMessage);
});

function sendMessage(event) {
    event.preventDefault();  // フォーム送信のデフォルト動作を防ぐ

    let userInput = document.getElementById("user-input").value;//user-input
    if (!userInput.trim()) return;  // 空入力を防ぐ

    let messages = document.getElementById("messages");
    messages.innerHTML += `<p><strong>あなた:</strong> ${userInput}</p>`;

    // API にリクエスト
    fetch("/chat", {
        method: "POST",
        body: JSON.stringify({ message: userInput }),
        headers: { "Content-Type": "application/json" }
    })
    .then(response => response.json())
    .then(data => {
        messages.innerHTML += `<p><strong>Gemini:</strong> ${data.reply}</p>`;
        document.getElementById("user-input").value = "";  // 入力フィールドをクリア
    })
    .catch(error => console.error("エラー:", error));
}
