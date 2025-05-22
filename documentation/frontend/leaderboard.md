## Leaderboard Platform Endpoints


`/leaderboard`
- Megjeleníti:
    - A legjobb felhasználó külön kiemelve (profilképpel, összpontszámmal, legjobb pontszámmal, frissítés idejével)
    - Az összes többi felhasználót egy táblázatban
    - Oldalanként 5 felhasználót listáz
    - Lapozás: Previous és Next gombokkal
- A lapozáshoz a limit=5 és page paraméterek kerülnek elküldésre
- A dinamikus betöltést a *leaderboard.js* végzi:
    - Az oldal betöltésekor meghívja a *loadLeaderboard(currentPage)* függvényt
    - A top-user div-be betölti a legmagasabb pontszámú felhasználót
    - A leaderboard-table táblázatban jeleníti meg az összes többi top játékost
    - A pagination div-be helyezi el az oldalváltó gombokat, és megjeleníti az aktuális oldalszámot (pl. Page 2 of 6)
    - Az oldalváltó gombok újra meghívják a *loadLeaderboard()* függvényt az új page értékkel
    - Ha nincs találat (res.ok === false), a hibaüzenet jelenik meg a topUser helyén
