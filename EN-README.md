#                               Q'Me Quiz App


## 1. System Specification

### Objective
**Q'Me** is a gamified online quiz platform that enables:
- User registration and login
- Completing quizzes with various difficulty levels and topics
- Viewing personal statistics and global results
- Submitting custom questions by users
- Viewing a leaderboard with profile pictures

### Development Tools
- Visual Studio Code, Postman, MySQL Workbench
- Flask, Python 3, Chart.js, HTML/CSS/JS
- Docker, Git, Pylance (VS Code plugin)

### Environment
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Database**: MySQL (in Docker container)
- **Platform**: Linux (Ubuntu), Windows 10+, vagy macOS


## 2. Requirements Specification

### Desired System Overview
The system supports user-driven learning through quizzes. Users can also submit their own questions, with built-in profanity filtering. Progress is tracked via statistical charts, age-based global averages, and a leaderboard.

### Required Business Processes
- Completing quizzes with score calculation based on difficulty multiplier
- Submitting questions to predefined topics
- User profile and password management
- Leaderboard display
- Profile picture upload (only certain formats)

### Requirements List
- Python 3.10+, Flask, MySQL, Docker
- Recommended OS: Ubuntu 22.04+, Windows 10+, macOS


## 3. Functional Specification

### Program Objective
Create an interactive, user-friendly quiz platform that encourages self-learning and creativity through user-submitted questions.

### Feature List
- Registration with birthdate (only for users 16+ years old)
- Profile picture upload and saving in supported formats (png, jpg, jpeg, svg)
- Login with JWT cookie-based authentication
- Completing quizzes with selected difficulty and topic
- Submitting questions with profanity filtering
- Personal statistics by topic (e.g., accuracy rate)
- Global statistics grouped by age
- Leaderboard based on scores and profile pictures

### Technical Operation
- Access Control Services (middleware):
    - Guest Guard:
        - Automatically blocks guest users from accessing authenticated pages
        - Allowed paths: /login, /register, /api/login, /api/register, /static/...
        - If guest calls an API unauthorized: 401 Unauthorized, if HTML page: redirect to /login
    - Auth Guard:
        - Prevents logged-in users from accessing guest-only pages (login, register)
        - Automatically redirects them to /home

Automatic Data Seeding
- Seed Data:
    - Populates the database using JSON files in the `data/` folder:
        - `user.json`: users
        - `topics.json`: topics
        - `questions.json`: questions and answers
        - `results.json`: results, scores, leaderboard
    - The `load_results()` function automatically::
        - calculates total and top scores
        - updates the leaderboard (LeaderBoard)
        - links answers and questions to the Result table

### Testing
- All feature endpoints tested manually via Postman
- Quiz logic validated: profanity handling, score calculation, filters
- Frontend tested on Chrome and Firefox browsers


## 4. Installation and Execution

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Prepare Database
```sh
mysql -u root -p
CREATE DATABASE quiz_app;
```

### Prepare .env
```.env
SECRET_KEY=TODO
JWT_SECRET_KEY=TODO
MYSQL_USER=root
MYSQL_PASSWORD=TODO
MYSQL_DB=quiz_app
MYSQL_HOST=localhost
MYSQL_PORT=3306
SQLALCHEMY_DATABASE_URI=TODO
```

### Start the Application
```sh
python3 app.py
```
This will launch the Flask app on port 8080 and automatically populate the database.


## 5. Available Endpoints and API Documentation

The full list and description of API endpoints are available in the following `.md` files:
```sh
EN-documentation
├── backend
│   ├── authAPI.md
│   ├── createQuizAPI.md
│   ├── leaderboardAPI.md
│   ├── quizAPI.md
│   └── statisticsAPI.md
└── frontend
    ├── auth.md
    ├── createQuiz.md
    ├── leaderboard.md
    ├── quiz.md
    └── statistics.md
```


## 6. Git and File Management

- `.gitignore` includes `__pycache__/`, `.env`, `*.sqlite3`, `static/images/profiles/`.
- Version control: Git + GitHub


## 7. License

**UNLICENSED**

This project is created for educational purposes. Deployment in production requires thorough security auditing and standardization.
