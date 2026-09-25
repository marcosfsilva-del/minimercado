const cpfInput = document.getElementById("cpf");

if (cpfInput) {
    cpfInput.addEventListener("input", (event) => {
        let cpf = event.target.value.replace(/\D/g, "");

        cpf = cpf.slice(0, 11);

        if (cpf.length > 9) {
            cpf = cpf.replace(
                /^(\d{3})(\d{3})(\d{3})(\d{1,2})$/,
                "$1.$2.$3-$4"
            );
        } else if (cpf.length > 6) {
            cpf = cpf.replace(
                /^(\d{3})(\d{3})(\d{1,3})$/,
                "$1.$2.$3"
            );
        } else if (cpf.length > 3) {
            cpf = cpf.replace(
                /^(\d{3})(\d{1,3})$/,
                "$1.$2"
            );
        }

        event.target.value = cpf;
    });
}