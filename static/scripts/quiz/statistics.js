document.addEventListener("DOMContentLoaded", async () => {
    try {
        const userRes = await fetch("/api/user-statistics");
        const globalRes = await fetch("/api/global-statistics");

        const userData = await userRes.json();
        const globalData = await globalRes.json();

        if (userRes.ok) renderUserChart(userData);
        if (globalRes.ok) renderGlobalChart(globalData);
    } catch (err) {
        console.error("Failed to load statistics:", err);
    }
});

function renderUserChart(data) {
    const ctx = document.getElementById("user-chart").getContext("2d");
    new Chart(ctx, {
        type: "bar",
        data: {
            labels: data.map(d => d.topic),
            datasets: [{
                label: "Correct Answer Rate (%)",
                data: data.map(d => d.averageCorrectAnswerRate),
                backgroundColor: "#717744"
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100
                }
            }
        }
    });
}

function renderGlobalChart(data) {
    const ctx = document.getElementById("global-chart").getContext("2d");
    new Chart(ctx, {
        type: "bar",
        data: {
            labels: data.map(d => d.age),
            datasets: [{
                label: "Average Score",
                data: data.map(d => d.ageCorrectAnswerRate),
                backgroundColor: "#8D5B4C"
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}
