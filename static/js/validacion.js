function validar_formulario(){
    var usuario = document.getElementById("usuario").value;
    var correo = document.getElementById("correo").value;
    var clave = document.getElementById("contrasena").value;
    var conf_clave = document.getElementById("conf_contrasena").value;
    var nombre = document.getElementById("nombre").value;
    var apellido = document.getElementById("apellido").value;
    var telefono = document.getElementById("telefono").value;
    
    if (usuario=="" || correo=="" || clave=="" ||nombre=="" || apellido=="" || telefono=="" || conf_clave==""){
        alert("Todos los campos son obligatorios")
        return false;
    }
    var usuario_len = usuario.value.length;
    if(usuario_len == 0 || usuario_len < 5){
       alert("Su usuario debe contener más de 5 caracteres");
       passid.focus();
    }

    var formatoCorreo = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if(!correo.value.match(formatoCorreo)){
       alert("El correo electronico debe ser válido!");
       correo.focus();
    }

    var passid_len = clave.value.length;
    if (passid_len == 0 || passid_len < 8){
       alert("La clave debe contener más de 8 caracteres");
       passid.focus();
    }
    
}

function showForm(){
    document.getElementById('inicio').style.display = "block";
}

function hideForm(){
    document.getElementById('inicio').style.display = "none";
}