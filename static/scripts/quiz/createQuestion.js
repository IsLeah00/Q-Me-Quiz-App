function showFormMessage(msg, type = "error") {
    const box = document.getElementById("form-message");
    box.textContent = msg;
    box.className = `form-message ${type}`;
    box.style.display = "block";
}

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("create-form");
    const addAnswerBtn = document.getElementById("add-answer");
    const answersSection = document.getElementById("answers-section");

    let answerCount = 0;

    function createAnswerInput() {
        if (answerCount >= 4) return;

        const wrapper = document.createElement("div");
        wrapper.innerHTML = `
            <input type="text" placeholder="Answer text" required class="answer-text">
            <label>
                <input type="radio" name="correct" class="correct-radio">
                Correct
            </label>
            <button type="button" class="remove-answer">X</button>
        `;
        wrapper.classList.add("answer-wrapper");
        answersSection.appendChild(wrapper);
        answerCount++;

        wrapper.querySelector(".remove-answer").addEventListener("click", () => {
            wrapper.remove();
            answerCount--;
        });
    }

    addAnswerBtn.addEventListener("click", createAnswerInput);

    const topicCheckboxes = document.querySelectorAll('input[name="topics"]');
    topicCheckboxes.forEach(cb => {
        cb.addEventListener("change", () => {
            const checked = document.querySelectorAll('input[name="topics"]:checked');
            if (checked.length > 4) {
                cb.checked = false;
                showFormMessage("You can select up to 4 topics only.");
            }
        });
    });

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        document.getElementById("form-message").style.display = "none";
        document.getElementById("profanity-warning").style.display = "none";

        const questionText = document.getElementById("questionText").value;
        const difficulty = document.getElementById("difficulty").value;
        const topicCheckboxes = document.querySelectorAll('input[name="topics"]:checked');
        const topics = Array.from(topicCheckboxes).map(cb => cb.value);

        const answerWrappers = document.querySelectorAll(".answer-wrapper");
        if (answerWrappers.length < 2) {
            showFormMessage("You must add at least 2 answers.");
        }

        const answers = [];
        let hasCorrect = false;
        answerWrappers.forEach((el, i) => {
            const text = el.querySelector(".answer-text").value;
            const isCorrect = el.querySelector(".correct-radio").checked;
            answers.push({ answerText: text, isCorrect });
            if (isCorrect) hasCorrect = true;
        });

        if (!hasCorrect) {
            showFormMessage("Please mark one answer as correct.");
        }

        const res = await fetch("/api/create-question", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ questionText, difficulty, topics, answers })
        });

        const data = await res.json();

        if (res.ok) {
            showFormMessage("Your question was created!", "success");
            form.reset();
            answersSection.innerHTML = "";
            answerCount = 0;
        } else if (data.censoredQuestion) {
            document.getElementById("profanity-warning").style.display = "block";
            document.getElementById("censored-question").textContent = data.censoredQuestion;
            const list = document.getElementById("censored-answers");
            list.innerHTML = "";
            data.censoredAnswers.forEach(a => {
                const li = document.createElement("li");
                li.textContent = a.answerText;
                list.appendChild(li);
            });
        } else {
            showFormMessage(data.error);
        }
    });
});
