// referenciar los elementos del DOM
const tickerSelectElement = document.getElementById('ticker-select');
const customTickerGroup = document.getElementById('custom-ticker-group');
const customTickerInput = document.getElementById('custom-ticker');
const btnSimulate = document.getElementById('btn-simulate');
const btnText = document.querySelector('.btn-text');
const btnLoader = document.querySelector('.loader');
const errorMessage = document.getElementById('error-message');

const valFinal = document.getElementById('val-final');
const valRentabilidad = document.getElementById('val-rentabilidad');

let portfolioChart = null;

// Mostrar/ocultar input custom
tickerSelectElement.addEventListener('change', (e) => {
    if (e.target.value === 'custom') {
        customTickerGroup.style.display = 'flex';
    } else {
        customTickerGroup.style.display = 'none';
    }
});

// Listener del boton
btnSimulate.addEventListener('click', async () => {
    errorMessage.style.display = 'none';

    // Obtener el ticker
    let ticker = tickerSelectElement.value;
    if (ticker === 'custom') {
        ticker = customTickerInput.value.trim().toUpperCase();
        if (!ticker) {
            showError("Por favor ingresa un Ticker válido.");
            return;
        }
    }

    // Set UI to loading state
    setLoadingState(true);

    try {
        const response = await fetch(`/api/simulate?ticker=${ticker}`);

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || "Error al procesar el activo.");
        }

        const data = await response.json();

        // Update DOM
        updateDashboard(data);
        renderChart(data);

    } catch (error) {
        showError(error.message);
    } finally {
        setLoadingState(false);
    }
});

function setLoadingState(isLoading) {
    btnSimulate.disabled = isLoading;
    if (isLoading) {
        btnText.style.display = 'none';
        btnLoader.style.display = 'block';
        valFinal.textContent = "Calculando...";
        valRentabilidad.textContent = "-- %";
        valRentabilidad.className = "metric-value";
    } else {
        btnText.style.display = 'block';
        btnLoader.style.display = 'none';
    }
}

function showError(msg) {
    errorMessage.textContent = `❌ ${msg}`;
    errorMessage.style.display = 'block';
    valFinal.textContent = "-- €";
    valRentabilidad.textContent = "-- %";
}

function updateDashboard(data) {
    valFinal.textContent = `${data.capital_final.toFixed(2)} €`;

    const isPositive = data.rentabilidad >= 0;
    const sign = isPositive ? "+" : "";

    valRentabilidad.textContent = `${sign}${data.rentabilidad.toFixed(2)} %`;
    valRentabilidad.className = `metric-value ${isPositive ? 'positive' : 'negative'}`;
}

function renderChart(data) {
    const ctx = document.getElementById('portfolioChart').getContext('2d');

    // Destruir grafico anterior si existe
    if (portfolioChart) {
        portfolioChart.destroy();
    }

    // Crear array de background colors dinamicos basándose en >= 100 o < 100
    // Chart.js supports segment styling nicely via context plugin or pre-computing gradients.
    // We will use a baseline of 100.

    portfolioChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.fechas,
            datasets: [
                {
                    label: 'Valor de la Cartera (€)',
                    data: data.valores_cartera,
                    borderColor: '#2f81f7',
                    borderWidth: 2,
                    pointRadius: 0,
                    pointHoverRadius: 5,
                    fill: {
                        target: { value: 100 },
                        above: 'rgba(63, 185, 80, 0.15)', // Verde suave si gana (arriba de 100)
                        below: 'rgba(248, 81, 73, 0.15)'  // Rojo suave si pierde (debajo de 100)
                    },
                    tension: 0.1
                },
                {
                    label: 'Baseline (100€)',
                    data: Array(data.fechas.length).fill(100),
                    borderColor: 'rgba(255, 255, 255, 0.3)',
                    borderWidth: 1,
                    borderDash: [5, 5],
                    pointRadius: 0,
                    fill: false
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            interaction: {
                mode: 'index',
                intersect: false,
            },
            plugins: {
                tooltip: {
                    backgroundColor: 'rgba(22, 27, 34, 0.9)',
                    titleColor: '#e6edf3',
                    bodyColor: '#e6edf3',
                    borderColor: 'rgba(255,255,255,0.1)',
                    borderWidth: 1,
                    callbacks: {
                        label: function (context) {
                            return `${context.dataset.label}: ${context.parsed.y.toFixed(2)} €`;
                        }
                    }
                },
                legend: {
                    labels: { color: '#8b949e' }
                }
            },
            scales: {
                x: {
                    grid: { color: 'rgba(255, 255, 255, 0.05)' },
                    ticks: { color: '#8b949e', maxTicksLimit: 10 }
                },
                y: {
                    grid: { color: 'rgba(255, 255, 255, 0.05)' },
                    ticks: { color: '#8b949e' }
                }
            }
        }
    });
}
