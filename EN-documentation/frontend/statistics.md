## Statistics Platform Endpoints


`/statistics`
- Displays user statistics in two interactive bar charts:
    1. Personal statistics: correct answer rate per topic (%)
    2. Global statistics: average score by age group
- Template file:
    - Loads *Chart.js* via CDN
    - Contains two *<canvas>* elements:
        - *#user-chart*: user’s personal performance
        - *#global-chart*: global statistics by age
- Dynamic behavior handled by *statistics.js*:
    - On page load, it fetches:
        - GET /api/user-statistics: current user's topic-based performance
        - GET /api/global-statistics: average score by age from all users
    - *Chart.js* renders both charts with the fetched data
- Visualizations:
    - *renderUserChart(data)*:
        - X-axis: topic names
        - Y-axis: averageCorrectAnswerRate (0–100%)
        - Bar color: #717744
    - *renderGlobalChart(data)*:
        - X-axis: age
        - Y-axis: ageCorrectAnswerRate (average score)
        - Bar color: #8D5B4C
    - If fetching or processing fails, error is logged in the console
