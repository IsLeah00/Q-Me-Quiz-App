## Quiz Endpoints


`/api/start-quiz`
- Bejelentkezéshez kötött
- Paraméterek: difficulty, topic
- A megadott nehézséghez és témához tartozó 5 véletlenszerű kérdést küld vissza
    - Legalább 5 érvényes kérdésnek kell lennie a témában (különben hibaüzenet)


`/api/submit-quiz`
- Paraméterek: válaszolt questionId, answerId, difficulty, topic
- Eredmények mentése a results, leaderboard táblákba
- Pontszám számítása:
    - Minden helyes válaszért: 1 * multiplier
        - Multiplier értéke:
                - easy: 1
                - medium: 2
                - hard: 3
