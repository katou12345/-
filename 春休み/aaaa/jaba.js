function sendMessage() {
    event.preventDefault();
    let userInput = document.getElementById("name").value;
    if (!userInput) return;

    let messages = document.getElementById("messages");
    messages.innerHTML += `<p><strong>���Ȃ�:</strong> ${userInput}</p>`;

    // API�Ƀ��N�G�X�g
    fetch("/chat", {
        method: "POST",
        body: JSON.stringify({ message: userInput }),
        headers: { "Content-Type": "application/json" }
    })
    .then(response => response.json())
    .then(data => {
        messages.innerHTML += `<p><strong>Gemini:</strong> ${data.reply}</p>`;
        document.getElementById(name).value = "";  // ���̓t�B�[���h���N���A"user-input"
    })
    .catch(error => console.error("�G���[:", error));
    document.getElementById("chat-form").addEventListener("submit", sendMessage);
}