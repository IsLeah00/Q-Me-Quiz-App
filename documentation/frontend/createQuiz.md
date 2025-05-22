## Create Quiz Platform Endpoints


`/get-creative`
- A felület, ahol bejelentkezett felhasználók saját kvízkérdéseket hozhatnak létre
- Tartalmazza:
    - Kérdés megadása (szövegdoboz)
    - Nehézség kiválasztása (easy, medium, hard)
    - minimum 1 maximum 4 téma kiválasztása checkboxokkal
    - minimum 2 maximum 4 válasz megadása, amelyek közül pontosan 1 megjelölhető helyesnek
    - Beküldő gomb: Submit Question
- A formhoz kapcsolódó *createQuestion.js*:
    - Dinamikusan ad hozzá vagy távolít el válasz mezőket (max 4)
    - Ellenőrzi, hogy legalább 2 válasz van, és pontosan 1 van kijelölve helyesnek
    - A beküldött kérdést elküldi a POST /api/create-question végpontra
    - Szitokszó-szűrés (server oldali better_profanity): ha trágár szó van, visszaküldi a cenzúrázott kérdést és válaszokat
    - A hibák és sikeres üzenetek a form-message dobozban jelennek meg
    - A sikeres kérdés után a form törlődik és újra használható
