## Auth Platform Endpoints


`/register`
- The registration form (*register.html*) is accessible at this route
- Collects username, birthdate, password, and profile picture
- On submission, the *register.js* JavaScript file sends a POST request to the /api/register endpoint
    - After a successful registration, automatic redirection to the login page after a few seconds
- Real-time password validation with *passwordCheck.js*:
    - at least 6 characters
    - uppercase and lowercase letters
    - number
    - special character
    - as each rule is fulfilled, the label turns green
- Toggle password visibility with 🙉 icon, handled by *passwordView.js*
- File upload:
    - Allowed formats: .png, .jpg, .jpeg, .svg
    - The image is automatically renamed to match the username and stored in the static/images/profiles/ folder


`/login`
- The login form (*login.html*) is available at this route
- Contains fields for username and password
- Password visibility toggle (🙈 / 🙉) also works here via *passwordView.js*
- On submission, *login.js* sends a POST request to the /api/login endpoint
- Feedback is displayed (form-message); on success, the user is redirected to the /home page


`/logout`
- The logout page (*logout.html*) asks for confirmation: "Are you sure?"
- Sends a POST request to /api/logout:
    - On success, the JWT cookie is cleared
    - Otherwise, the user is redirected back to the login page (*auth_routes.py*)
- Includes a “No, take me back” button which navigates back to /home
