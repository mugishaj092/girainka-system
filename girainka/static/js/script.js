document.addEventListener("DOMContentLoaded", () => {
    const reportCounts = JSON.parse(document.getElementById("reportCounts").textContent);

    const body = document.querySelector("body"),
        modeToggle = body.querySelector(".mode-toggle");

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
                        label: "Monthly Reports",
                        data: Object.values(reportCounts), // Use report data from backend
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

    // Initial render of the chart
    renderChart();

    // Mode toggle event
    modeToggle.addEventListener("click", () => {
        body.classList.toggle("dark");
        renderChart();
    });
});
