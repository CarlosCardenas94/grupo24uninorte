function suma(numero1, numero2){
    return numero1 + numero2;
}

function calculo(numero1, numero2, callback){
    return callback(numero1, numero2);
}

function sumar(){
    let a = parseInt(document.getElementById("a").value);
    let b = parseInt(document.getElementById("b").value);
    document.getElementById("result").innerHTML = "El resultado de la suma es " + calculo(a,b,suma);
}