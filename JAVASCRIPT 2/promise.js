const login = () => {
    return new Promise((resolve, reject) => {
        if (true){
            resolve("Bienvenido");
        }
        else{
            reject("Hubo un error");
        }
    })
}

login()
.then(response => console.log(response))
.catch(err => console.error(err));