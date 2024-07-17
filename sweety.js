document.addEventListener('DOMContentLoaded', () => {
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    const chatLog = document.getElementById('chat-log');

    sendBtn.addEventListener('click', () => {
        const message = userInput.value.trim();
        if (message) {
            appendMessage('user', message);
            fetchBotResponse(message);
            userInput.value = '';
        }
    });

    userInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            sendBtn.click();
        }
    });

    function appendMessage(sender, text) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', sender === 'user' ? 'user-message' : 'bot-message');
        messageDiv.innerText = text;
        chatLog.appendChild(messageDiv);
        chatLog.scrollTop = chatLog.scrollHeight;
    }

    function fetchBotResponse(message) {
        fetch('http://localhost:5000/ask_sweety', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            appendMessage('bot', data.response);
        })
        .catch(error => {
            console.error('Error:', error);
            appendMessage('bot', 'There was an error processing your request.');
        });
    }
});
