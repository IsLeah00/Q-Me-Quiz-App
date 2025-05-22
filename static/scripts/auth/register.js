document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const messageBox = document.getElementById("form-message");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        messageBox.style.display = "none";

        const formData = new FormData(form);

        const res = await fetch("/api/register", {
            method: "POST",
            body: formData
        });

        const data = await res.json();

        messageBox.textContent = data.message || data.error;
        messageBox.className = `form-message ${res.ok ? "success" : "error"}`;
        messageBox.style.display = "block";

        if (res.ok) {
            setTimeout(() => {
                window.location.href = "/login";
            }, 3000);
        }
    });
});
