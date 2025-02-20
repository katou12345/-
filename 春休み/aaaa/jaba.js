function sendMessage() {
    event.preventDefault();
    let userInput = document.getElementById("name").value;
    if (!userInput) return;

    let messages = document.getElementById("messages");
    messages.innerHTML += `<p><strong>あなた:</strong> ${userInput}</p>`;

    // APIにリクエスト
    fetch("/chat", {
        method: "POST",
        body: JSON.stringify({ message: userInput }),
        headers: { "Content-Type": "application/json" }
    })
    .then(response => response.json())
    .then(data => {
        messages.innerHTML += `<p><strong>Gemini:</strong> ${data.reply}</p>`;
        document.getElementById(name).value = "";  // 入力フィールドをクリア"user-input"
    })
    .catch(error => console.error("エラー:", error));
    document.getElementById("chat-form").addEventListener("submit", sendMessage);
}