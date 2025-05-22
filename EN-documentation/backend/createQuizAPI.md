## Create Quiz Endpoints


`/api/create-question`
- Only accessible to logged-in users
- Required fields: questionText, difficulty, topics[], answers[]
    - Exactly 1 answer must be marked as correct
    - A minimum of 2 and a maximum of 4 answers must be provided
    - Automatic profanity filter (using better_profanity library) applied to both question and answers
        - If offensive content is detected, the censored version is returned with an error
