function calcularDV(rut) {
  let suma = 0;
  let multiplo = 2;

  for (let i = rut.length - 1; i >= 0; i--) {
    suma += parseInt(rut.charAt(i)) * multiplo;
    multiplo = multiplo === 7 ? 2 : multiplo + 1;
  }

  const resto = 11 - (suma % 11);
  if (resto === 11) return "0";
  if (resto === 10) return "K";
  return resto.toString();
}

function validarRut(rutNumero, rutDV) {
  if (!/^\d{7,8}$/.test(rutNumero)) return false;
  const dvCalculado = calcularDV(rutNumero);
  return dvCalculado === rutDV.toUpperCase();
}

function guardarFicha() {
  const rutNumero = document.getElementById("rutNumero").value.trim();
  const rutDV = document.getElementById("rutDV").value.trim().toUpperCase();
  const nombres = document.getElementById("nombres").value.trim();
  const apellidoPaterno = document
    .getElementById("apellidoPaterno")
    .value.trim();
  const apellidoMaterno = document
    .getElementById("apellidoMaterno")
    .value.trim();
  const direccion = document.getElementById("direccion").value.trim();
  const ciudad = document.getElementById("ciudad").value.trim();
  const telefono = document.getElementById("telefono").value.trim();
  const email = document.getElementById("email").value.trim();
  const nacimiento = document.getElementById("nacimiento").value;
  const estadoCivil = document.getElementById("estadoCivil").value;
  const comentarios = document.getElementById("comentarios").value.trim();
  const nombreRegex = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ]+(?:\s[a-zA-ZáéíóúÁÉÍÓÚñÑ]+)*$/;

  // Validación de nombres
  if (!nombres || !nombreRegex.test(nombres)) {
    alert("Ingrese un nombre válido (solo letras y espacios).");
    return;
  }

  // Validación de apellidos
  if (!apellidoPaterno || !nombreRegex.test(apellidoPaterno)) {
    alert("Ingrese un apellido paterno válido (solo letras).");
    return;
  }
  if (!apellidoMaterno || !nombreRegex.test(apellidoMaterno)) {
    alert("Ingrese un apellido materno válido (solo letras).");
    return;
  }

// Validación de email
const emailRegex = /^[a-zA-Z0-9._-]+@(gmail\.com|hotmail\.com|outlook\.com)$/;
if (!emailRegex.test(email)) {
  alert("Email inválido. Ingrese un correo electrónico válido (solo Gmail, Hotmail, o Outlook).");
  return;
}

  // Validación de fecha de nacimiento
  const hoy = new Date().toISOString().split("T")[0];
  if (!nacimiento || nacimiento > hoy) {
    alert("Fecha de nacimiento inválida. No se puede seleccionar una fecha futura.");
    return;
  }

  // Validación de RUT
  if (!validarRut(rutNumero, rutDV)) {
    alert("RUT inválido. Ingrese RUT válido.");
    return;
  }

  // Validación de teléfono
  if (!/^\d{7,15}$/.test(telefono)) {
    alert("Teléfono inválido. Solo números y entre 7 a 15 dígitos.");
    return;
  }

  // Validación de email
  if (!email.includes("@")) {
    alert("Email inválido.");
    return;
  }

  const rutCompleto = `${rutNumero}-${rutDV}`;
  const ficha = {
    rut: rutCompleto,
    nombres,
    apellidoPaterno,
    apellidoMaterno,
    direccion,
    ciudad,
    telefono,
    email,
    nacimiento,
    estadoCivil,
    comentarios,
  };

  if (localStorage.getItem(rutCompleto)) {
    if (!confirm("¿Deseas sobrescribir este registro?")) return;
  }

  localStorage.setItem(rutCompleto, JSON.stringify(ficha));
  document.getElementById("fichaForm").reset();

  alert("Ficha guardada correctamente.");
  window.location.href = "agradecimiento.html";
}

function buscarPorApellido() {
  const apellidoBuscado = document
    .getElementById("buscarApellido")
    .value.trim()
    .toLowerCase();

  for (let key in localStorage) {
    if (localStorage.hasOwnProperty(key)) {
      try {
        const ficha = JSON.parse(localStorage.getItem(key));
        if (
          ficha.apellidoPaterno &&
          ficha.apellidoPaterno.toLowerCase() === apellidoBuscado
        ) {
          sessionStorage.setItem("pacienteBuscado", JSON.stringify(ficha));
          window.location.href = "datosBusqueda.html";
          return;
        }
      } catch (e) {
        console.error("Error al leer una ficha:", e);
      }
    }
  }

  alert("No se encontró ningún paciente con ese apellido paterno.");
}


