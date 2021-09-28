
/* Botón para confirmar un cierre */
/* let confirmacion = confirm("¿Estás seguro que desas salir?") */  /* Cuadro de dialogo con dos alternativas */

/* if (confirmacion){
    setTimeout("cerrar()", 5000);
    document.write("Esta pagina se cerrara")
    function cerrar(){
        window.close();
    }
}  */

/* Objeto navigator */
/* alert("Navegador: " + navigator.appVersion);
alert("Idioma: " + navigator.language); */

/* location.reload(); */

let raizCuadrada = Math.sqrt(25);
/* alert(raizCuadrada); */
let fecha = new Date();
let dia = fecha.getDate();
let mes = fecha.getMonth() +1;
let anio = fecha.getFullYear();

console.log(fecha);
console.log(dia);
console.log(mes);
console.log(anio);

let mayus = "Carlos".toUpperCase();
console.log(mayus);

function teclaPresionada() {
    /* alert("Presionaste una tecla") */
}

function foco(x){
    x.style.background = "#5EFF78";
    
}

function sinFoco(){
    let x = document.getElementById("nombre");
    x.value = x.value.toUpperCase();
}
