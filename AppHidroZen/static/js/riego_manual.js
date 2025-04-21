document.addEventListener('DOMContentLoaded', function() {
    const manualSwitch = document.getElementById('manualSwitch');
    const deactivateManualButton = document.getElementById('deactivateManual'); // Ya no se usa directamente
    const activateTimedButton = document.getElementById('activateTimed');
    const manualDurationInput = document.getElementById('manualDuration');
    const manualStatusText = document.getElementById('manualStatus');
    const manualFeedbackDiv = document.getElementById('manualFeedback');
    const switchLabel = document.querySelector('.switch-label');

    let isRiegoManualActivo = false; // Variable para rastrear el estado

    function actualizarEstadoRiego(activo) {
        isRiegoManualActivo = activo;
        manualStatusText.textContent = activo ? 'Activo' : 'Inactivo';
        manualStatusText.className = activo ? 'activo' : 'inactivo';
        manualSwitch.checked = activo;
        switchLabel.textContent = activo ? 'Encendido' : 'Apagado';
        activateTimedButton.disabled = activo;
    }

    function mostrarMensaje(mensaje, tipo = 'info') {
        manualFeedbackDiv.textContent = mensaje;
        manualFeedbackDiv.className = `manual-feedback ${tipo}`; // Aseguramos que siempre esté la clase base 'manual-feedback'
        setTimeout(() => {
            manualFeedbackDiv.textContent = '';
            manualFeedbackDiv.className = 'manual-feedback'; // Volvemos a la clase base para limpiar estilos específicos
        }, 3000);
    }

    manualSwitch.addEventListener('change', function() {
        const activar = this.checked;
        const url = activar ? '/api/riego/manual/activar/' : '/api/riego/manual/desactivar/';
        const mensajeEstado = activar ? 'activado' : 'desactivado';
        const tipoMensaje = activar ? 'success' : 'desactivado'; // Usamos 'desactivado' como tipo
    
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                actualizarEstadoRiego(activar);
                mostrarMensaje(`Riego manual ${mensajeEstado}.`, tipoMensaje);
            } else {
                mostrarMensaje(`Error al ${mensajeEstado} el riego manual: ` + data.error, 'error');
                this.checked = !activar;
                actualizarEstadoRiego(!activar);
            }
        })
        .catch(error => {
            mostrarMensaje('Error de conexión: ' + error, 'error');
            this.checked = !activar;
            actualizarEstadoRiego(!activar);
        });
    });

    // Evento para activar el riego por una duración específica (sin cambios)
    activateTimedButton.addEventListener('click', function() {
        // ... (tu código existente para activar por duración) ...
    });

    function getCookie(name) {
        // ... (tu función existente para obtener la cookie CSRF) ...
    }
});