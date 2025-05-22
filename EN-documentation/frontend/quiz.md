## Quiz Platform Endpoints


`/home`
- The main page where users can start a new quiz
- Uses two dropdowns to select:
    - Topic
    - Difficulty (easy / medium / hard)
- The *location.reload()* is used to refresh the page at the end of a quiz
- The quiz interaction is entirely dynamic, controlled by *quizFlow.js*:
    - If there aren't enough questions in the selected category, an error message is shown
    - quizData is filled with questions from the returned JSON
        - The start-form’s submit event triggers the *showQuestion()* function
        - The quiz-section updates dynamically with the current question and answers
    - *submitAnswer()* adds each response to the *selectedAnswers* array
        - After the 5th question, it calls *finishQuiz()*
        - Then sends a POST request to /api/submit-quiz
- *renderChart()* displays the results in a pie chart (*Chart.js*):
    - Correct vs. incorrect answers
    - Colors: #647744 and #863c3c
