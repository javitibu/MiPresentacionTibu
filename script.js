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

