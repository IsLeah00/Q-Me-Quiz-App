## Auth Endpoints


`/api/register`
- Regisztráció csak 16 év felett (születési dátum ellenőrzés alapján)
- Kötelező mezők: felhasználónév, jelszó, születési dátum
    - Jelszónak tartalmaznia kell: kisbetű, nagybetű, szám, speciális karakter, legalább 6 karakter hossz
- Profilkép-feltöltés támogatott formátumai: .png, .jpg, .jpeg, .svg
    - Ha a fájl kiterjesztése nem támogatott, hibát küld vissza
    - A fájl automatikusan átnevezésre kerül a regisztrált felhasználónév alapján (pl. bob.png)
    - A kép mentése a következő helyre történik: static/images/profiles/
    - A fájl mentési útvonal automatikusan létrejön, ha nem létezik
    - A feltöltés opcionális, ha nincs fájl, akkor null értékkel kerül tárolásra


`/api/login`
- Bejelentkezés JWT sütialapú azonosítással
- Helyes felhasználónév-jelszó pár esetén tokent ad vissza


`/api/logout`
- Kijelentkezteti a felhasználót az authentikációs cookie törlésével.
