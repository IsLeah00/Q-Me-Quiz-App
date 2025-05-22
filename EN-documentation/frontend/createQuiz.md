## Create Quiz Platform Endpoints


`/get-creative`
- Interface where logged-in users can create their own quiz questions
- Includes:
    - Question input (textarea)
    - Difficulty selection (easy, medium, hard)
    - 1 to 4 topics selectable via checkboxes
    - 2 to 4 answer options, with exactly 1 marked as correct
    - Submit button: Submit Question
- Related script: *createQuestion.js*
    - Dynamically adds/removes answer input fields (max 4)
    - Validates that at least 2 answers are present and exactly 1 is correct
    - Sends submitted question via POST to /api/create-question
    - Profanity filter (server-side better_profanity): if inappropriate content is - detected, the censored version is returned
    - Errors and success messages are displayed in the form-message box
    - After successful submission, the form resets for reuse
