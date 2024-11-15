// Esta parte de js es para mostrar u ocultar secciones de contenido
function showSection(sectionId) {
    // Primero oculto todas las secciones
    const sections = document.querySelectorAll('.content-section');
    sections.forEach(section => {
        section.style.display = 'none';
    });

    // para mostrar la sección seleccionada
    const sectionToShow = document.getElementById(sectionId);
    sectionToShow.style.display = 'block';

    // Forzar el reajuste de la posición del video en la sección "¿Quién Soy?" que nose que le pasa
    if (sectionId === 'quien-soy') {
        const videoContainer = document.querySelector('.video-container');
        
        // Resetea el margen y los estilos de visualización
        videoContainer.style.marginTop = '1.5rem'; // Reaplica el margen superior

        // para que el video esté centrado, sin importar lo que se haga previamente
        videoContainer.style.display = 'none'; // Oculto el contenedor
        videoContainer.offsetHeight; // fuerzo el redibujado (reflow)
        videoContainer.style.display = 'flex'; // para mostrar de nuevo con el estilo correctamente aplicado
    }
}

// Función de validación para el formulario de contacto
function validateForm() {
    // Obtener los valores de los campos del formulario
    const nombreApellido = document.getElementById('nombre-apellido').value;
    const correo = document.getElementById('correo').value;
    const motivo = document.getElementById('motivo').value;

    // Verificar si los campos obligatorios están vacíos
    if (!nombreApellido || !correo || !motivo) {
        // Mostrar el mensaje de error
        document.getElementById('error-message').style.display = 'block';
        return false; // No se envía el formulario
    }

    // Si todos los campos obligatorios están completos, ocultar el mensaje de error
    document.getElementById('error-message').style.display = 'none';

    // Mostrar el mensaje de agradecimiento
    document.getElementById('thank-you-message').style.display = 'block';

    // Limpiar el formulario
    document.getElementById('contact-form').reset();

    // Evitar que el formulario se recargue
    return false;
}
