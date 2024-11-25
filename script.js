// Función para mostrar u ocultar secciones de contenido
function showSection(event, sectionId) {
    event.preventDefault(); // esto evita el comportamiento predeterminado del enlace

    // Ocultar todas las secciones
    const sections = document.querySelectorAll('.content-section');
    sections.forEach(section => {
        section.style.display = 'none';
    });

    // Mostrar la sección seleccionada
    const sectionToShow = document.getElementById(sectionId);
    if (sectionToShow) {
        sectionToShow.style.display = 'block';
    }
}

// Función de validación para el formulario de contacto
function validateForm() {
    const nombreApellido = document.getElementById('nombre-apellido').value;
    const correo = document.getElementById('correo').value;
    const motivo = document.getElementById('motivo').value;

    if (!nombreApellido || !correo || !motivo) {
        document.getElementById('error-message').style.display = 'block';
        return false;
    }

    document.getElementById('error-message').style.display = 'none';
    document.getElementById('thank-you-message').style.display = 'block';
    document.getElementById('contact-form').reset();
    return false;
}
// Función para consumir la API y mostrar los productos
const apiUrl = 'https://miapi.com/obtener-productos';

// Lista de experiencias predefinidas
const experienciasPredefinidas = [
    "CSS",
    "JavaScript",
    "Python",
    "React",
    "Node.js",
    "Desarrollo Web",
    "Bases de Datos"
];

// Función para cargar las experiencias predefinidas en el select
function cargarExperiencias() {
    const select = document.getElementById('intereses-predefinidos');
    
    // Limpio el select antes de agregar nuevas opciones
    select.innerHTML = '';

    // Creo la opción por defecto
    const opcionDefault = document.createElement('option');
    opcionDefault.value = '';
    opcionDefault.textContent = '-- Selecciona una opción --';
    select.appendChild(opcionDefault);

    // Agrego las opciones predefinidas
    experienciasPredefinidas.forEach(experiencia => {
        const opcion = document.createElement('option');
        opcion.value = experiencia;
        opcion.textContent = experiencia;
        select.appendChild(opcion);
    });
}

// Función para enviar la selección de intereses
function enviarIntereses() {
    const experienciaSeleccionada = document.getElementById('intereses-predefinidos').value;
    const experienciaPersonalizada = document.getElementById('experiencia-personalizada').value;

    // Compruevo qué opción se ha seleccionado o escrito
    let mensaje = "Experiencias seleccionadas:\n";

    if (experienciaSeleccionada) {
        mensaje += `- Predefinida: ${experienciaSeleccionada}\n`;
    }

    if (experienciaPersonalizada) {
        mensaje += `- Personalizada: ${experienciaPersonalizada}\n`;
    }

    if (!experienciaSeleccionada && !experienciaPersonalizada) {
        mensaje = "No se ha seleccionado ninguna experiencia.";
    }

    // Mostrar la información en consola o procesarla, ver esta parte
    console.log(mensaje);

    // Limpiar el formulario después de enviar
    document.getElementById('experiencia-personalizada').value = '';
    document.getElementById('intereses-predefinidos').value = '';
}

// Cargar las experiencias predefinidas cuando se cargue la página
document.addEventListener("DOMContentLoaded", cargarExperiencias);

document.addEventListener("DOMContentLoaded", () => {
    const navbarCollapse = document.getElementById("navbarNav"); // El contenedor colapsable
    const navLinks = document.querySelectorAll(".navbar-nav .nav-link"); // Todos los enlaces del menú

    navLinks.forEach(link => {
        link.addEventListener("click", () => {
            const bsCollapse = new bootstrap.Collapse(navbarCollapse, { toggle: false });
            bsCollapse.hide(); // Cierra el menú
        });
    });
});
