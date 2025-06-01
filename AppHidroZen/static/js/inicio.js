const canvas = document.getElementById("particleCanvas");
const ctx = canvas.getContext("2d");
const progressBar = document.getElementById('progressBar');
const progressValue = document.getElementById('progressValue');
const progressFill = document.getElementById('progressFill');
const programButton = document.getElementById('programButton');
const modal = document.getElementById('modal');
const modalMessage = document.getElementById('modalMessage');
const closeButton = document.getElementById('closeButton');
const datePicker = document.getElementById('datePicker');
const timePicker = document.getElementById('timePicker');
const durationSlider = document.getElementById('durationSlider');
const durationValue = document.getElementById('durationValue');

// Ajustar el tamaño del canvas
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Mostrar valor de humedad en tiempo real
progressBar.addEventListener('input', function () {
    const value = progressBar.value;
    progressValue.textContent = `${value}%`;
    progressFill.style.width = `${value}%`;
});

// Mostrar valor de duración en tiempo real
durationSlider.addEventListener('input', function () {
    durationValue.textContent = durationSlider.value;
});

// Botón de programar
programButton.addEventListener('click', function () {
    const humidity = progressBar.value;
    const date = datePicker.value;
    const time = timePicker.value;
    const duration = durationSlider.value;

    if (!humidity || humidity < 5 || !date || !time) {
        modalMessage.textContent = "Por favor, completa todos los datos correctamente. La humedad debe ser mayor al 5%.";
        modal.style.display = 'flex';
        return;
    }

    const esp32IP = "http://192.168.20.7";
    const timestamp = new Date().getTime();

    // Mostrar en consola la URL que se va a usar
    console.log(`[DEBUG] Enviando a: ${esp32IP}/set-duracion?segundos=${duration}&_=${timestamp}`);
    console.log(`[DEBUG] Enviando a: ${esp32IP}/programar?humedad=${humidity}&fecha=${date}&hora=${time}&_=${timestamp}`);

    // 1. Enviar duración
    fetch(`${esp32IP}/set-duracion?segundos=${duration}&_=${timestamp}`)
        .then(response => response.text())
        .then(data => console.log("Duración configurada:", data))
        .catch(error => console.error("Error en duración:", error));

    // 2. Enviar parámetros de programación
    fetch(`${esp32IP}/programar?humedad=${humidity}&fecha=${date}&hora=${time}&_=${timestamp}`)
        .then(response => response.text())
        .then(data => {
            modalMessage.textContent = data;
            modal.style.display = 'flex';
        })
        .catch(error => {
            console.error("Error al enviar programación:", error);
            modalMessage.textContent = "Error al conectar con el servidor del sistema de riego.";
            modal.style.display = 'flex';
        });
});


// Botón cerrar modal
closeButton.addEventListener('click', function () {
    modal.style.display = 'none';
});

// Animación de partículas
let particles = [];
for (let i = 0; i < 50; i++) {
    particles.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        radius: Math.random() * 4 + 1.5,
        speedX: Math.random() * 1.5 - 0.75,
        speedY: Math.random() * 1.5 - 0.75,
        color: "rgba(30, 144, 255, 0.7)"
    });
}

function animateParticles() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach(p => {
        ctx.beginPath();
        ctx.fillStyle = p.color;
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fill();

        p.x += p.speedX;
        p.y += p.speedY;

        if (p.x < 0 || p.x > canvas.width) p.speedX *= -1;
        if (p.y < 0 || p.y > canvas.height) p.speedY *= -1;
    });
    requestAnimationFrame(animateParticles);
}
animateParticles();



