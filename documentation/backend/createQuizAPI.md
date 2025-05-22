## Create Quiz Endpoints


`/api/create-question`
- Kizárólag bejelentkezett felhasználók használhatják
- Kötelező mezők: questionText, difficulty, topics[], answers[]
    - Pontosan 1 helyes választ kell megadni
    - Összesen minimum 2 és maximum 4 válasz adható meg
    - Automatikus obszcenitásszűrés (better_profanity library) a kérdésre és válaszokra
        - Cenzúrázott verzió visszaküldve hibával, ha sértő tartalom észlelhető
