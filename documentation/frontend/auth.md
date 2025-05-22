## Auth Platform Endpoints


`/register`
- A regisztrációs űrlap (*register.html*) elérhető ezen az útvonalon
- Felhasználónév, születési dátum, jelszó és profilkép bekérése
- Elküldéskor a *register.js* JavaScript fájl POST kérést küld a /api/register API végpontra
    - Sikeres regisztráció után automatikus átirányítás a login oldalra pár másodperc után
- Valós idejű jelszóvalidáció a *passwordCheck.js* segítségével:
    - legalább 6 karakter
    - kis- és nagybetű
    - szám
    - speciális karakter
    - amint teljesül egy szabály zöldszínű lesz
- Jelszó megjelenítés váltása: a 🙉 ikon *passwordView.js*-el működik
- Fájl feltöltés:
    - .png, .jpg, .jpeg, .svg kiterjesztés engedélyezett
    - a kép automatikusan a static/images/profiles/ mappába kerül, név szerint átnevezve és formátumot megtartva


`/login`
- A bejelentkezési űrlap (*login.html*) ezen az útvonalon érhető el
- Felhasználónév és jelszó mezők
- A jelszót itt is meg lehet jeleníteni vagy elrejteni (🙈 / 🙉) a *passwordView.js*-el
- Elküldés után a *login.js* JavaScript fájl POST kérést küld a /api/login végpontra
- Visszajelzés jelenik meg (form-message), siker esetén átirányít /home oldalra


`/logout`
- A kijelentkező oldal (logout.html) megerősítést kér: "Are you sure?"
- POST kérelem küldése /api/logout-ra:
    - Sikeres esetben a JWT cookie törlésre kerül
    - Másképp visszairányítás a login oldalra (auth_routes.py)
- Tartalmaz „No, take me back” gombot, amely visszavisz a főoldalra (/home)
