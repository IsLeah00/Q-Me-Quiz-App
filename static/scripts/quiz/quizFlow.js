let quizData = [];
let currentIndex = 0;
let selectedAnswers = [];
let difficulty = "";
let topic = "";

function showFormMessage(msg, type = "error") {
    const box = document.getElementById("form-message");
    box.textContent = msg;
    box.className = `form-message ${type}`;
    box.style.display = "block";
}

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("start-form");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        difficulty = document.getElementById("difficulty").value;
        topic = document.getElementById("topic").value;

        document.getElementById("form-message").style.display = "none";

        const res = await fetch("/api/start-quiz", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ difficulty, topic })
        });

        if (res.redirected) {
            window.location.href = res.url;
            return;
        }

        const data = await res.json();
        if (res.ok) {
            quizData = data.quiz;
            currentIndex = 0;
            selectedAnswers = [];
            document.getElementById("start-section").style.display = "none";
            showQuestion();
        } else {
            showFormMessage(data.error);
        }
    });
});

function showQuestion() {
    const container = document.getElementById("quiz-section");
    const question = quizData[currentIndex];
    container.innerHTML = `
        <h2>Question ${currentIndex + 1} of 5</h2>
        <p>${question.questionText}</p>
        <div class="answers">
            ${question.answers.map(a => `
                <button onclick="submitAnswer(${a.answerId}, ${question.questionId})">${a.answerText}</button>
            `).join("")}
        </div>
    `;
    container.style.display = "block";
}

async function submitAnswer(answerId, questionId) {
    selectedAnswers.push({ questionId, answerId });
    currentIndex++;

    if (currentIndex < quizData.length) {
        showQuestion();
    } else {
        await finishQuiz();
    }
}

async function finishQuiz() {
    const res = await fetch("/api/submit-quiz", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            answers: selectedAnswers,
            difficulty,
            topic
        })
    });

    const data = await res.json();
    if (res.ok) {
        document.getElementById("quiz-section").style.display = "none";
        document.getElementById("result-section").style.display = "block";

        renderChart(data.correct, data.total);

        const scoreDiv = document.getElementById("final-score");
        scoreDiv.innerText = `You scored ${data.score} points with a ${data.multiplier}x multiplier.`;
    } else {
        showFormMessage(data.error);
    }
}

function renderChart(correct, total) {
    const ctx = document.getElementById("result-chart").getContext("2d");
    new Chart(ctx, {
        type: "pie",
        data: {
            labels: ["Correct", "Incorrect"],
            datasets: [{
                data: [correct, total - correct],
                backgroundColor: ["#647744", "#863c3c"]
            }]
        },
        options: {
            plugins: {
                legend: {
                    position: "bottom"
                }
            }
        }
    });
}
