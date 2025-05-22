## Leaderboard Platform Endpoints


`/leaderboard`
- Displays:
    - The top user highlighted separately (with profile picture, total score, top score, updated time)
    - All other users in a table
    - Pagination: shows 5 users per page
    - Navigation via Previous and Next buttons
- Pagination uses limit=5 and page query parameters
- The *leaderboard.js* handles dynamic behavior:
    - On page load, it calls *loadLeaderboard(currentPage)*
    - Fills the top-user div with the highest scoring user
    - Populates the leaderboard-table with other top users
    - Places navigation buttons inside the pagination div and shows the current page (e.g., Page 2 of 6)
    - Navigation buttons re-trigger *loadLeaderboard()* with the new page
    - If no data (res.ok === false), an error message appears in place of topUser
