function submitMessage() {
	const user_input = document.getElementById('input').value;
	const chatLog = document.getElementById('chat-log');
	const converter = new showdown.Converter();
	const placeholder = document.getElementById('placeholder');

	if (user_input.trim() !== '') {
		const messageHtml = `<div class="chat-message user-message">${user_input}</div>`;
		chatLog.innerHTML += messageHtml;
		document.getElementById('input').value = '';
		if (placeholder) placeholder.style.display = 'none';
	}

	if (chatLog.innerHTML.trim() === '') {
		if (placeholder) placeholder.style.display = 'flex';
	}
	fetch('/get', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/x-www-form-urlencoded',
		},
		body: 'msg=' + encodeURIComponent(user_input)
	})
		.then(response => response.json())
		.then(data => {
			const messageHtml = converter.makeHtml(data.message);
			chatLog.innerHTML += `<div class="chat-message user-message">Você:<br> ${user_input}<br></div>`;
			chatLog.innerHTML += `<div class="chat-message bot-message">Guará:<br> ${messageHtml}</div>`;
			document.getElementById('input').value = '';
		})
		.catch(error => console.error('Error:', error));
}

document.addEventListener('DOMContentLoaded', function () {
	const inputField = document.getElementById('input');

	inputField.addEventListener('keypress', function (event) {
		if (event.key === 'Enter') {
			event.preventDefault();  // Evita qualquer ação padrão do Enter
			submitMessage();  // Chama a função que você já tem para enviar mensagens
		}
	});
});