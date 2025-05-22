## Statistics Platform Endpoints


`/statistics`
- Megjeleníti a felhasználó statisztikáit két interaktív oszlopdiagram formájában:
    1. Saját statisztika: helyes válaszarány témánként (%)
    2. Globális statisztika: átlagos pontszám korcsoportonként
- A sablonfájl:
    - Betölti a *Chart.js* könyvtárat (CDN-en keresztül)
        - Két <canvas> elemet tartalmaz:
            - #user-chart: a felhasználó saját teljesítménye
            - #global-chart: globális koralapú statisztika
- A dinamikus működést a *statistics.js* biztosítja:
    - Az oldal betöltésekor lekérdezi:
        - GET /api/user-statistics: az aktuális felhasználó statisztikáit témánként
        - GET /api/global-statistics: összes felhasználó életkora alapján számolt átlagpontszámát
    - A válaszadatokat a Chart.js könyvtár segítségével megjeleníti
- Vizualizációk:
    - *renderUserChart(data)*:
        - Témák nevét (topic) használja x-tengelyen
        - Oszlopérték: averageCorrectAnswerRate (0-100%)
        - Háttérszín: #717744
    - *renderGlobalChart(data)*:
        - X-tengely: életkor
        - Y-tengely: ageCorrectAnswerRate (átlagos pontszám)
        - Háttérszín: #8D5B4C
    - Amennyiben a lekérés vagy feldolgozás sikertelen, az error logolásra kerül a konzolban.
