let table = new DataTable('#tabela', {
    // options
});

document.getElementById("toggleSenha").addEventListener("click", function () {
    const senha = document.getElementById("senha");
    const icone = document.getElementById("iconeOlho");

    if (senha.type === "password") {
        senha.type = "text";
        icone.classList.remove("fa-eye");
        icone.classList.add("fa-eye-slash");
    } else {
        senha.type = "password";
        icone.classList.remove("fa-eye-slash");
        icone.classList.add("fa-eye");
    }
});

