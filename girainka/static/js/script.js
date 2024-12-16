document.addEventListener("DOMContentLoaded", () => {
    // Chart logic
    let reportCounts = {};
    try {
        const reportData = document.getElementById("reportCounts").textContent;
        reportCounts = JSON.parse(reportData);
    } catch (error) {
        console.error("Failed to parse reportCounts JSON:", error);
    }

    const body = document.querySelector("body"),
        modeToggle = body.querySelector(".mode-toggle");
    body.classList.add("dark");

    function getChartColors() {
        return body.classList.contains("dark")
            ? {
                  textColor: "#ffffff",
                  gridColor: "#444444",
                  tooltipBackground: "#333333",
                  borderColor: "#0EBF3F",
              }
            : {
                  textColor: "#0d2030",
                  gridColor: "#e0e0e0",
                  tooltipBackground: "#0EBF3F",
                  borderColor: "#0EBF3F",
              };
    }

    let chartInstance;
    function renderChart() {
        const chartColors = getChartColors();

        if (chartInstance) {
            chartInstance.destroy();
        }

        const ctx = document.getElementById("chart");
        Chart.defaults.font.family = "Poppins";

        chartInstance = new Chart(ctx, {
            type: "line",
            data: {
                labels: [
                    "Jan",
                    "Feb",
                    "Mar",
                    "Apr",
                    "May",
                    "Jun",
                    "Jul",
                    "Aug",
                    "Sep",
                    "Oct",
                    "Nov",
                    "Dec",
                ],
                datasets: [
                    {
                        label: "Monthly Reports",
                        data: Object.values(reportCounts),
                        backgroundColor: "transparent",
                        borderColor: chartColors.borderColor,
                        cubicInterpolationMode: "monotone",
                        fill: false,
                    },
                ],
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false,
                    },
                    title: {
                        display: true,
                        text: "Monthly Report Performance",
                        color: chartColors.textColor,
                        font: { size: 16, weight: "normal" },
                    },
                    tooltip: {
                        backgroundColor: chartColors.tooltipBackground,
                        bodyColor: "#fff",
                        cornerRadius: 4,
                    },
                },
                scales: {
                    x: {
                        ticks: { color: chartColors.textColor },
                        grid: { color: chartColors.gridColor },
                    },
                    y: {
                        title: {
                            display: true,
                            text: "Reports",
                            color: chartColors.textColor,
                        },
                        ticks: {
                            padding: 5,
                            color: chartColors.textColor,
                        },
                        grid: { color: chartColors.gridColor },
                    },
                },
            },
        });
    }
    renderChart();
    modeToggle.addEventListener("click", () => {
        body.classList.toggle("dark");
        renderChart();
    });

    document.querySelectorAll(".action-btn.delete").forEach((btn) => {
        btn.addEventListener("click", function () {
            const userId = this.getAttribute("data-id");

            if (confirm("Are you sure you want to delete this user?")) {
                fetch(`/delete-user/${userId}/`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": getCookie("csrftoken"), // Ensure CSRF token is included
                    },
                })
                    .then((response) => {
                        if (!response.ok) {
                            throw new Error("Failed to delete user.");
                        }
                        return response.json();
                    })
                    .then((data) => {
                        if (data.success) {
                            alert(data.message);
                            const userRow = document.getElementById(`user-${userId}`);
                            if (userRow) {
                                userRow.remove();
                            }
                            window.location.reload();
                        } else {
                            alert(data.message);
                        }
                    })
                    .catch((error) => {
                        console.error("Error:", error);
                        alert("An error occurred. Please try again.");
                    });
            }
        });
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split(";");
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + "=")) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});

document.addEventListener("DOMContentLoaded", () => {
  const viewButtons = document.querySelectorAll(".action-btn.view");
  const modal = document.getElementById("userModal");
  const closeButton = document.querySelector(".close-btn");
  const userDetailsDiv = document.getElementById("userDetails");

  // Function to open the modal and load user details
  function openModal(userId) {
    // Send AJAX request to get user data (assuming you have a URL endpoint like /get-user/<id>/)
    fetch(`/get-user/${userId}/`)
      .then(response => response.json())
      .then(data => {
        if (data.success) {
          const user = data.user;
          userDetailsDiv.innerHTML = `
            <p><strong>Email:</strong> ${user.email}</p>
            <p><strong>First Name:</strong> ${user.firstName}</p>
            <p><strong>Last Name:</strong> ${user.lastName}</p>
            <p><strong>Address:</strong> ${user.address}</p>
            <p><strong>Role:</strong> ${user.role}</p>
            <p><strong>Verified:</strong> ${user.verified ? "Yes" : "No"}</p>
            <p><strong>Created At:</strong> ${user.created_at}</p>
          `;
          modal.style.display = "block"; // Show the modal
        } else {
          alert("Failed to load user data.");
        }
      })
      .catch(error => {
        console.error("Error:", error);
        alert("An error occurred while loading user data.");
      });
  }

  // Attach event listeners to view buttons
  viewButtons.forEach(btn => {
    btn.addEventListener("click", function() {
      const userId = this.getAttribute("data-id");
      openModal(userId); // Open modal for the clicked user
    });
  });

  // Close the modal when the close button is clicked
  closeButton.addEventListener("click", () => {
    modal.style.display = "none";
  });

  // Close the modal if the user clicks outside of the modal
  window.addEventListener("click", (event) => {
    if (event.target === modal) {
      modal.style.display = "none";
    }
  });

  var path = window.location.pathname;

    // Remove any previous active classes from all menu items
    var menuItems = document.querySelectorAll('.nav-links li');
    menuItems.forEach(function(item) {
        item.classList.remove('active');
    });

    // Add active class based on the current URL path
    if (path.includes('/dashboard/')) {
        document.getElementById('dashboard-link').classList.add('active');
    } else if (path.includes('/dashboard/cows/')) {
        document.getElementById('cows-link').classList.add('active');
    } else if (path.includes('/dashboard/users/')) {
        document.getElementById('users-link').classList.add('active');
    } else if (path.includes('/dashboard/reports/')) {
        document.getElementById('reports-link').classList.add('active');
    } else if (path.includes('/dashboard/messages/')) {
        document.getElementById('messages-link').classList.add('active');
    } else if (path.includes('/dashboard/sources/')) {
        document.getElementById('sources-link').classList.add('active');
    }
});
