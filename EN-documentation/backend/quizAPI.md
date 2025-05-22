## Quiz Endpoints


`/api/start-quiz`
- Requires login
- Parameters: difficulty, topic
- Returns 5 random questions for the given difficulty and topic
    - There must be at least 5 valid questions in the topic, otherwise an error is returned


`/api/submit-quiz`
- Parameters: submitted questionId, answerId, difficulty, topic
- Saves results to results and leaderboard tables
- Score calculation:
    - Each correct answer earns: 1 * multiplier
        - Multiplier values:
                - easy: 1
                - medium: 2
                - hard: 3
