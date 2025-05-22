let currentPage = 1;
const limit = 5;

document.addEventListener("DOMContentLoaded", () => {
    loadLeaderboard(currentPage);

    document.body.addEventListener("click", (e) => {
        if (e.target.id === "next-page") {
            currentPage++;
            loadLeaderboard(currentPage);
        }
        if (e.target.id === "prev-page") {
            currentPage--;
            loadLeaderboard(currentPage);
        }
    });
});

async function loadLeaderboard(page) {
    const res = await fetch(`/api/leaderboard?page=${page}&limit=${limit}`);
    const data = await res.json();

    const topContainer = document.getElementById("top-user");
    const tbody = document.querySelector("#leaderboard-table tbody");
    const table = document.getElementById("leaderboard-table");

    tbody.innerHTML = "";

    if (!res.ok) {
        topContainer.innerHTML = `<p>${data.error}</p>`;
        table.style.display = "none";
        return;
    }

    const top = data.topUser;
    topContainer.innerHTML = `
        <div class="user-row">
            <img src="/static/images/profiles/${top.profilePic}" class="profile-pic" onerror="this.src='/static/images/q-me-logo.png'">
            <div class="user-info">
                <h3>${top.username}</h3>
                <p><strong>Total Score:</strong> ${top.totalScore}</p>
                <p><strong>Top Score:</strong> ${top.topScore}</p>
                <p><strong>Updated At:</strong> ${top.updatedAt}</p>
            </div>
        </div>
    `;

    data.others.forEach(entry => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>
                <div class="user-cell">
                    <img src="/static/images/profiles/${entry.profilePic}" class="profile-pic" onerror="this.src='/static/images/q-me-logo.png'">
                    <span>${entry.username}</span>
                </div>
            </td>
            <td>${entry.totalScore}</td>
            <td>${entry.topScore}</td>
            <td>${entry.updatedAt}</td>
        `;
        tbody.appendChild(row);
    });

    const pagination = document.getElementById("pagination");
    pagination.innerHTML = "";

    const pageInfo = document.createElement("span");
    pageInfo.textContent = `Page ${data.currentPage} of ${data.totalPages}`;
    pageInfo.style.margin = "0 10px";
    pageInfo.style.fontWeight = "bold";

    if (data.hasPrev) {
        const prevBtn = document.createElement("button");
        prevBtn.id = "prev-page";
        prevBtn.textContent = "Previous";
        pagination.appendChild(prevBtn);
    }

    pagination.appendChild(pageInfo);

    if (data.hasNext) {
        const nextBtn = document.createElement("button");
        nextBtn.id = "next-page";
        nextBtn.textContent = "Next";
        pagination.appendChild(nextBtn);
    }
}
