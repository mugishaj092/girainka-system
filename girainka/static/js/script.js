const body = document.querySelector("body"),
      modeToggle = body.querySelector(".mode-toggle"),
      sidebar = body.querySelector("nav"),
      sidebarToggle = body.querySelector(".sidebar-toggle");

let getMode = localStorage.getItem("mode");
if (getMode && getMode === "dark") {
    body.classList.toggle("dark");
}

let getStatus = localStorage.getItem("status");
if (getStatus && getStatus === "close") {
    sidebar.classList.toggle("close");
}

// Function to get colors dynamically based on mode
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
        chartInstance.destroy(); // Destroy existing chart instance
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
                    label: "Monthly Mybrand performance",
                    data: [
                        2235, 3250, 1890, 5400, 20240, 6254, 12325, 4856, 10325,
                        2254, 22356, 8486,
                    ],
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
                    text: "Monthly Mybrand performance",
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
                        text: "Visitors",
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

// Initial render of the chart
renderChart();

// Mode toggle event
modeToggle.addEventListener("click", () => {
    body.classList.toggle("dark");
    if (body.classList.contains("dark")) {
        localStorage.setItem("mode", "dark");
    } else {
        localStorage.setItem("mode", "light");
    }
    renderChart();
});

sidebarToggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");
    if (sidebar.classList.contains("close")) {
        localStorage.setItem("status", "close");
    } else {
        localStorage.setItem("status", "open");
    }
});

createIcons({ icons });