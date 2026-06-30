const selector = document.getElementById('formSelec');
const servicio = document.getElementById('formSer');
const evento = document.getElementById('formEvent');
const nombre = document.getElementById('formNombre');
const fecha = document.getElementById('formDate');
const hora = document.getElementById('formTime');
const direccion = document.getElementById('formDir');
let value = selector.value
const form = document.getElementById('formContacto')
let today = new Date().toLocaleDateString('en-CA'); 
const labelDir = document.getElementById('labelDir')
const labelEve = document.getElementById('labelEve')
const labelSer = document.getElementById('labelSer')
  
fecha.min = today;



selector.addEventListener('change', activarCampos);
form.addEventListener('submit', whatsapp)

//Hace que solo esté activo el campo de servicio o evento que tú elijas
function activarCampos() {
    value = selector.value

   if (value == 'ser') {
        servicio.removeAttribute('disabled')
        evento.setAttribute('disabled', 'true')
        labelDir.innerHTML = ''
        servicio.setAttribute('required','true')
        evento.removeAttribute('required')
        direccion.removeAttribute('required')
        labelEve.innerHTML = ''
        labelSer.innerHTML = '*'
    }

    if (value == 'eve') {
        servicio.setAttribute('disabled', 'true')
        evento.removeAttribute('disabled')
        labelDir.innerHTML = '*'
        evento.setAttribute('required','true')
        servicio.removeAttribute('required')
        direccion.setAttribute('required','true')
        labelEve.innerHTML = '*'
        labelSer.innerHTML = ''
    }
}

activarCampos()

function whatsapp() {
    //Convierte la fecha de formato mm/dd/yyyy a texto natural
    const partes = fecha.value.split('-');
    const fechaD = new Date(partes[0], partes[1] - 1, partes[2]);
    const opciones = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    let fechaNatural = fechaD.toLocaleDateString('es-ES', opciones);

    //Esta linea simplemente quita la coma en la fecha
    fechaNatural = fechaNatural.replace(',', '')

    let mensaje = ''
    //En evento, revisa la opcion seleccionada y de esa saca la data de 'pronombre'
    let pronombre = evento.options[evento.selectedIndex].dataset.pronombre;



    //Mensajes para whatsapp, separados segun para que es el contacto

    if (value == 'ser') {
        mensaje = `Hola, soy ${nombre.value}. Me interesa el servicio de ${servicio.value} para el ${fechaNatural} a las ${hora.value} en ${direccion.value}.

¿Podría darme más información? Quedo en espera de una respuesta, gracias`;
    }

    if (value == 'eve') {
        mensaje = `Hola, soy ${nombre.value}. Me interesa la cobertura de ${pronombre} ${evento.value} para el ${fechaNatural} a las ${hora.value} en ${direccion.value}.

¿Podría darme más información?  Quedo en espera de una respuesta, gracias`;
    }

    //Telefono debe incluir el codigo de pais
    const encode = encodeURIComponent(mensaje)
    const telefono = '5214431681214'

    const url = `https://wa.me/${telefono}?text=${encode}`;

    open(url, '_blank')


}
