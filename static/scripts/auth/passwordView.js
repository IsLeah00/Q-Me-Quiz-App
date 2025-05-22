document.addEventListener("DOMContentLoaded", function () {
    const toggle = document.getElementById("togglePassword");
    const password = document.getElementById("password");

    toggle.addEventListener("click", function () {
        const type = password.type === "text" ? "password" : "text";
        password.type = type;
        toggle.textContent = type === "text" ? "🙈" : "🙉";
    });
});
