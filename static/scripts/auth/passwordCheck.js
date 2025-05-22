document.addEventListener("DOMContentLoaded", function () {
    const passwordInput = document.getElementById("password");

    const rules = {
        length: document.getElementById("length"),
        uppercase: document.getElementById("uppercase"),
        lowercase: document.getElementById("lowercase"),
        number: document.getElementById("number"),
        special: document.getElementById("special"),
    };

    passwordInput.addEventListener("input", function () {
        const value = passwordInput.value;
        rules.length.classList.toggle("valid", value.length >= 6);
        rules.uppercase.classList.toggle("valid", /[A-Z]/.test(value));
        rules.lowercase.classList.toggle("valid", /[a-z]/.test(value));
        rules.number.classList.toggle("valid", /\d/.test(value));
        rules.special.classList.toggle("valid", /[\W_]/.test(value));
    });
});
