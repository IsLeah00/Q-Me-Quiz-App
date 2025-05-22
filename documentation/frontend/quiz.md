## Quiz Platform Endpoints


`/home`
- A kezdőoldal, ahonnan a felhasználó elindíthat egy új kvízt
- Két lenyíló mező segítségével választhat:
    - Téma (topic)
    - Nehézség (difficulty: easy / medium / hard)
- a *location.reload()* az oldal újratöltésére szolgál a quiz végén
- A quiz interakció teljes egészében dinamikus, a *quizFlow.js* irányítja:
    - Ha nincs elég kérdés a kiválasztott kategóriában, hibaüzenetet jelenít meg
    1. A quizData feltöltése a kapott JSON adatokkal
        - Az űrlap (start-form) submit eseménye meghívja a *showQuestion()* függvényt
        - A quiz-section rész dinamikusan frissül a kérdés + válaszgombok alapján
    2. A *submitAnswer()* minden kattintással hozzáad egy választ a *selectedAnswers* tömbhöz
        - Az 5. kérdés után meghívja a *finishQuiz()* függvényt
        - Ekkor POST-olja a válaszokat a /api/submit-quiz végpontra
- A *renderChart()* megjeleníti az eredményt egy kördiagramon (*Chart.js*):
    - Helyes vs. helytelen válaszok
    - Színek: #647744 és #863c3c
