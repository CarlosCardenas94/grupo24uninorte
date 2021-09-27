function validar_formulario(){

    let name = document.getElementById("nombre");
    let name_length = name.value.length;
    if (name_length == 0){
        alert("El campo Nombre no puede estar vacio");
    }

    let user = document.getElementById("usuario");
    let user_length = user.value.length;
    if (user_length == 0 ){
        alert("El campo Usuario no puede estar vacio");
    }
    if (user_length < 8){ 
        alert("El campo usuario no puede tener menos de 8 caracteres")
    }

    let pass = document.getElementById("contrasena");
    let pass_length = pass.value.length;
    if (user_length == 0 ){
        alert("El campo Contraseña no puede estar vacio");
    }
    if (pass_length < 8){
        alert("La contrseña debe tener más de 8 caracteres");
        document.getElementById("contrasena").innerHTML = "La clave debe tener más de 8 caracteres";
    }

    
}