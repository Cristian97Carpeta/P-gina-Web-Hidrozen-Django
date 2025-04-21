const canvas = document.getElementById("particleCanvas");
const ctx = canvas.getContext("2d");
const progressBar = document.getElementById('progressBar');
const progressValue = document.getElementById('progressValue');
const progressFill = document.getElementById('progressFill');
const programButton = document.getElementById('programButton');
const modal = document.getElementById('modal');
const modalMessage = document.getElementById('modalMessage');
const closeButton = document.getElementById('closeButton');

// Ajusta el tamaño del canvas para cubrir toda la ventana
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

programButton.addEventListener('click', function () {
    const humidity = progressBar.value;
    const date = document.getElementById('datePicker').value;
    const time = document.getElementById('timePicker').value;

    if (!humidity || !date || !time) {
        modalMessage.textContent = "Por favor, completa todos los datos antes de programar. La Humedad mayor a 5%";
    } else {
        modalMessage.textContent = "¡Programación exitosa!";
    }

    modal.style.display = 'block';
});

closeButton.addEventListener('click', function () {
    modal.style.display = 'none';
});

progressBar.addEventListener('input', function () {
    const value = progressBar.value;
    progressValue.textContent = `${value}%`;
    progressFill.style.width = `${value}%`;
});

let particles = [];
for (let i = 0; i < 50; i++) {
    particles.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        radius: Math.random() * 4 + 1.5,
        speedX: Math.random() * 1.5 - 0.75,
        speedY: Math.random() * 1.5 - 0.75,
        color: "rgba(30, 144, 255, 0.7)" // Color de las partículas
    });
}

// Función para animar las partículas
function animateParticles() {
    ctx.clearRect(0, 0, canvas.width, canvas.height); // Borra el contenido del canvas
    particles.forEach(p => {
        ctx.beginPath();
        ctx.fillStyle = p.color;
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2); // Dibuja las partículas
        ctx.fill();
        p.x += p.speedX; // Actualiza la posición en X
        p.y += p.speedY; // Actualiza la posición en Y
    });
    requestAnimationFrame(animateParticles); // Llama a la función recursivamente
}

// Inicia la animación de partículas
animateParticles();



