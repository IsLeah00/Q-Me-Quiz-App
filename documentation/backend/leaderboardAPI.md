## Leaderboard Endpoints


`/api/leaderboard?page=1&limit=5`
- Visszaadja az aktuális oldalon található legjobb felhasználók listáját.
    - A válasz tartalmazza:
        - username, profilePic, totalScore, topScore, updatedAt
    - Az első helyezett (topUser) külön szerepel a válaszban.
- Támogatott funkciók:
    - Lapozás: page és limit paraméterekkel
    - Frissítési időpont visszaadása (ha nincs, akkor now() kerül be)
