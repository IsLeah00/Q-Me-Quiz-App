## Leaderboard Endpoints


`/api/leaderboard?page=1&limit=5`
- Returns the list of top users for the current page
    - The response includes:
        - username, profilePic, totalScore, topScore, updatedAt
    - The top-ranked user (topUser) is returned separately in the response
- Supported features:
    - Pagination via page and limit query parameters
    - Includes last updated timestamp (or uses now() if not present)
