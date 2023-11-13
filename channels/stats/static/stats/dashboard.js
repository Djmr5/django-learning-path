//console.log("Hello World!");

const dashboardSlug = document.getElementById('dashboard-slug').textContent.trim();
const user = document.getElementById('user').textContent.trim();
const dataInput = document.getElementById('data-input');
const submitBtn = document.getElementById('submit-btn');
const dataBox = document.getElementById('data-box');

const socket = new WebSocket(`ws://${window.location.host}/ws/${dashboardSlug}/`);

socket.onmessage = function (e) {
    const { message, sender } = JSON.parse(e.data);
    dataBox.innerHTML += `<p><strong>${sender}</strong>: ${message}</p>`;
    updateChart();
};

submitBtn.addEventListener('click', function (e) {
    e.preventDefault();
    const dataValue = dataInput.value;
    socket.send(JSON.stringify({
        'message': dataValue,
        'sender': user,
    }));
});

const fetchChartData = async () => {
    const response = await fetch(window.location.href + 'chart/');
    const data = await response.json();
    //console.table(data);
    return data;
};

const ctx = document.getElementById('myChart').getContext('2d');
let chart;

const drawChart = async () => {
    const data = await fetchChartData();
    const { chartData, chartLabels } = data;

    chart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: chartLabels,
            datasets: [{
                label: 'Votes',
                data: chartData,
                borderWidth: 1,
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            },
            responsive: true,
            maintainAspectRatio: false,
        }
    });
};

const updateChart = async () => {
    if (chart) chart.destroy();
    await drawChart();
}

drawChart()
