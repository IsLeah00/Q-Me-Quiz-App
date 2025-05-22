#                               Q'Me Quiz App


## 1. Rendszerspecifikáció

### Feladat
A **Q'Me** egy játékosított online kvízplatform, amely lehetőséget nyújt:
- Felhasználók regisztrációjára és bejelentkezésére
- Kvízek kitöltésére különböző nehézségi szinteken és témakörökben
- Egyéni statisztikák és globális eredmények megtekintésére
- Kreatív kérdésbeküldésre felhasználók részéről
- Ranglisták megtekintésére profilképekkel

### Fejlesztői eszközök
- Visual Studio Code, Postman, MySQL Workbench
- Flask, Python 3, Chart.js, HTML/CSS/JS
- Docker, Git, Pylance (VS Code plugin)

### Környezet
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Adatbázis**: MySQL (Docker konténerben)
- **Platform**: Linux (Ubuntu), Windows 10+, vagy macOS


## 2. Követelményspecifikáció

### Vágyálom rendszer leírása
A rendszer támogatja a felhasználók kvízjátékkal történő tanulását. Egyéni kérdésbeküldési lehetőség is biztosított, beépített trágárságszűrővel. A felhasználók fejlődését statisztikai grafikonok, korosztályos átlagok, valamint ranglista segíti.

### Igényelt üzleti folyamatok
- Kvíz kitöltése, pontszámítás nehézségi szorzóval
- Kérdésbeküldés a szerkesztett témákhoz
- Felhasználói profil- és jelszókezelés
- Leaderboard megjelenítés
- Képfeltöltés profilhoz (csak bizonyos formátumok)

### Követelménylista
- Python 3.10+, Flask, MySQL, Docker
- Javasolt operációs rendszer: Ubuntu 22.04+, Windows 10+, macOS


## 3. Funkcionális specifikáció

### Program célkitűzése
Egy interaktív, felhasználóbarát kvízplatform létrehozása, amely ösztönzi az önálló tanulást, és támogatja a felhasználók kreativitását a saját kérdések beküldésével.

### Funkciók listája
- Regisztráció születési dátummal (csak 16+ éves felhasználóknak)
- Profilkép feltöltés és mentés támogatott formátumokkal (png, jpg, jpeg, svg)
- Bejelentkezés JWT sütialapú hitelesítéssel

- Kvíz kitöltése nehézségi és témaválasztással
- Kérdésbeküldés obszcenitásszűréssel
- Egyéni statisztikák témák szerint (pl. pontossági arány)
- Globális statisztikák korcsoportokra bontva
- Ranglista pontszámok és profilképek szerint

### Technikai működés
Hozzáférésvédelmi szolgáltatások (middleware):
- Guest Guard:
    - Automatikusan blokkolja a vendégfelhasználók hozzáférését olyan oldalakhoz, melyek hitelesítést igényelnek.
    - Engedélyezett utak: /login, /register, /api/login, /api/register, /static/...
    - Ha a vendég API-t hív jogosulatlanul: 401 Unauthorized, ha HTML oldalt: redirect /login
- Auth Guard:
    - Megakadályozza, hogy már bejelentkezett felhasználók elérjék a vendégoldalakat (login, regisztráció).
    - Automatikusan átirányítja őket a /home oldalra.

Automatikus adatfeltöltés (seedelés)
- Seed Data:
    - A `data/` mappában található JSON fájlok alapján feltölti az adatbázist:
        - `user.json`: felhasználók
        - `topics.json`: témák
        - `questions.json`: kérdések és válaszok
        - `results.json`: eredmények, pontszámok, leaderboard
    - A `load_results()` függvény automatikusan:
        - kiszámolja az összpontszámot és top score-t
        - frissíti a ranglistát (LeaderBoard)
        - hozzárendeli a válaszokat és kérdéseket a Result táblához

### Tesztelés
- Minden funkció végpontjai manuálisan tesztelve lettek Postmannel
- Kvízlogika validálva: trágárságkezelés, pontszámítás, szűrések
- Frontend funkciók Chrome és Firefox böngészőkön tesztelve


## 4. Telepítés és futtatás

### Függőségek telepítése
```sh
pip install -r requirements.txt
```

### Adatbázis előkészítés
```sh
mysql -u root -p
CREATE DATABASE quiz_app;
```

### Alkalmazás indítása
```sh
python3 app.py
```
Ez elindítja a Flask alkalmazást a 8080-as porton és automatikusan feltölti az adatbázist.


## 5. Elérhető végpontok és API dokumentációik

Az összes API végpont listája és leírása elérhető a következő `.md` fájlokban:
```sh
documentation
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


## 6. Git és fájlkezelés

- A `.gitignore` tartalmazza a `__pycache__/`, `.env`, `*.sqlite3`, `static/images/profiles/` fájlokat.
- Verziókezelés: Git + GitHub


## 7. License

**UNLICENSED**

Ez a projekt oktatási céllal készült, valós környezetbe telepítés előtt átfogó biztonsági audit és szabványosítás szükséges.
