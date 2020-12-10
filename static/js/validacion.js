function validar_formulario(){
    var usuario = document.getElementsByName("usuario").values;
    var correo = document.getElementsByName("correo").values;
    var clave = document.getElementsByName("contrasena").values;
    var conf_clave = document.getElementsByName("conf_contrasena").values;
    var nombre = document.getElementsByName("nombre").values;
    var apellido = document.getElementsByName("apellido").values;
    var telefono = document.getElementsByName("telefono").values;
    
    if (usuario=="" || correo=="" || clave=="" ||nombre=="" || apellido=="" || telefono=="" || conf_clave==""){
        alert("Todos los campos son obligatorios")
        return false;
    }
    else if(usuario.length == 0 || usuario.length < 5){
       alert("Su usuario debe contener más de 5 caracteres");
       passid.focus();
    }
    
    var formatoCorreo = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if(!correo.value.match(formatoCorreo)){
       alert("El correo electronico debe ser valido!");
       correo.focus();
    }

    var passid_len = clave.value.length;
    if (passid_len == 0 || passid_len < 8){
       alert("La clave debe contener más de 8 caracteres");
       passid.focus();
    }
    
}

// function showForm(){
//     document.getElementById('inicio').style.display = "block";
// }

// function hideForm(){
//     document.getElementById('inicio').style.display = "none";
// }