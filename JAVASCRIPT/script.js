/* document.write("Hola Mundo")

let nombre = "Carlos";

alert("Hola " + nombre);

let estado = true;
let numero1 = 100;
let numero2 = 120;

alert(numero1 + numero2);

let mascota; */
/* 
let num1 = parseInt(prompt("Escribe un numero"));
let num2 = parseInt(prompt("Escribe otro numero"));
alert("La suma de los numeros es: " + (num1 + num2)); */

/* let visitante = prompt("Escribe tu nombre");
alert("Bienvenido " + visitante);
 */
/* CONDICIONALES
let edad = parseInt(prompt("Escribe tu edad"))
if (edad >= 18)  {
    alert("Usted es mayor de edad");
    document.write("Usted es mayor edad");
}
else{
    alert("Usted es menor de edad");
    document.write("Usted es menor de edad");
} */

/* let stock = 15;
let cantidad = parseInt(prompt("Ingresa la cantidad a comprar"));
if (cantidad > stock){
    alert("La cantidad supera los productos en Stock")
} */


/* Ejemplo
let nombre = prompt("Escribe tu nombre");
let apellido = prompt("Escribe tu apellido");
let edad = parseInt(prompt("Escribe tu edad"));

document.write("Nombre: "+ nombre +" "+ apellido);
document.write(" Edad: " + edad); */

/* CICLO FOR */
/* let cantidad = parseInt(prompt("Ingrese la cantidad de Productos"));
let valor, total = 0;
for (let i = 0; i < cantidad; i++){
    valor = parseInt(prompt("Ingrese el valor del producto "+ (i+1)))
    total += valor;
}
alert("El total a pagar por los productos es: " + total); */

/* let cantidad = parseInt(prompt("Ingrese la cantidad de Edades a registrar"));
let edad, total = 0;
for (let i = 0; i < cantidad; i++){
    edad = parseInt(prompt("Ingrese la edad "+ (i+1)))
    total += edad;
}
alert("La suma total de las edades es: " + total); */

/* CICLO WHILE */
/* let j = 0, sumanota=0, promedio=0, nota;
let cantidadnotas = parseInt(prompt("Escribe la cantidad de notas"));

while (j < cantidadnotas){
    nota = parseFloat(prompt("Escribe la nota" + (j+1)));
    sumanota += nota;
    j++;
}
promedio = sumanota/cantidadnotas;
alert("El promedio de las notas es: " + promedio); */

/* CICLO DO WHILE */
/* let usuario, contrasena;
do {
    usuario = prompt("Ingresa tu usuario");
    contrasena = prompt("Ingres tu contraseña");
} while ((usuario !== "admin") && (contrasena !== "admin")); */
let num1, num2;
function sumar(){
    num1 = parseInt(prompt("Ingresa un numero"));
    num2 = parseInt(prompt("Ingresa otro numero"));
    alert("La suma de los numeros es: " + (num1 + num2));
}


