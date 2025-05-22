## Auth Endpoints


`/api/register`
- Registration allowed only for users aged 16+ (based on birthdate check)
- Required fields: username, password, birthdate
    - Password must include: lowercase letter, uppercase letter, number, special character, and be at least 6 characters long
- Profile picture upload – supported formats: .png, .jpg, .jpeg, .svg
    - If the file format is not supported, an error is returned
    - The file is automatically renamed to match the username (e.g., bob.png)
    - Image is saved under: static/images/profiles/
    - The target directory is created if it does not exist
    - Upload is optional; if not provided, null will be stored


`/api/login`
- Login using JWT cookie-based authentication
- Returns a token upon successful username-password match


`/api/logout`
- Logs out the user by clearing the authentication cookie
