// Referencias DOM Generales
const tickerSelectElement = document.getElementById('ticker-select');
const customTickerGroup = document.getElementById('custom-ticker-group');
const customTickerInput = document.getElementById('custom-ticker');
const btnAction = document.getElementById('btn-action');
const btnText = document.querySelector('.btn-text');
const btnLoader = document.querySelector('.loader');
const errorMessage = document.getElementById('error-message');

// Referencias DOM Simulador
const valFinal = document.getElementById('val-final');
const valRentabilidad = document.getElementById('val-rentabilidad');
let portfolioChart = null;

// Referencias DOM Escáner
const scanPeriodo = document.getElementById('scan-periodo');
const scanPorcentaje = document.getElementById('scan-porcentaje');
const scanTotal = document.getElementById('scan-total');
const scanTableBody = document.getElementById('scan-table-body');

// Variables de estado
let activeTab = 'simulator-section'; // 'simulator-section' o 'scanner-section'

// Lógica de Pestañas (Tabs)
document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
        // Quitar active a todos
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.tool-section').forEach(s => s.style.display = 'none');
        document.querySelectorAll('.tool-controls').forEach(c => c.style.display = 'none');

        // Activar el pulsado
        e.target.classList.add('active');
        activeTab = e.target.getAttribute('data-target');

        // Mostrar sección correspondiente
        document.getElementById(activeTab).style.display = 'flex';

        // Mostrar controles correspondientes en el sidebar
        if (activeTab === 'simulator-section') {
            document.getElementById('sim-controls').style.display = 'block';
            btnText.textContent = "Ejecutar Simulación";
        } else {
            document.getElementById('scan-controls').style.display = 'block';
            btnText.textContent = "Escanear Subidas";
        }

        errorMessage.style.display = 'none';
    });
});

// Mostrar/ocultar input custom de Ticker
tickerSelectElement.addEventListener('change', (e) => {
    if (e.target.value === 'custom') {
        customTickerGroup.style.display = 'flex';
    } else {
        customTickerGroup.style.display = 'none';
    }
});

function getTicker() {
    let ticker = tickerSelectElement.value;
    if (ticker === 'custom') {
        ticker = customTickerInput.value.trim().toUpperCase();
        if (!ticker) {
            throw new Error("Por favor ingresa un Ticker válido.");
        }
    }
    return ticker;
}

// Global Action Button Listener
btnAction.addEventListener('click', async () => {
    errorMessage.style.display = 'none';

    try {
        const ticker = getTicker();
        setLoadingState(true);

        if (activeTab === 'simulator-section') {
            await runSimulator(ticker);
        } else if (activeTab === 'scanner-section') {
            await runScanner(ticker);
        }
    } catch (error) {
        showError(error.message);
    } finally {
        setLoadingState(false);
    }
});

// --- LÓGICA SIMULADOR ---
async function runSimulator(ticker) {
    const response = await fetch(`/api/simulate?ticker=${ticker}`);
    if (!response.ok) {
        const data = await response.json();
        throw new Error(data.detail || "Error al procesar el activo.");
    }
    const data = await response.json();

    // Update Dashboard Metrics
    valFinal.textContent = `${data.capital_final.toFixed(2)} €`;
    const isPositive = data.rentabilidad >= 0;
    valRentabilidad.textContent = `${isPositive ? "+" : ""}${data.rentabilidad.toFixed(2)} %`;
    valRentabilidad.className = `metric-value ${isPositive ? 'positive' : 'negative'}`;

    // Render Chart
    renderChart(data);
}

function renderChart(data) {
    const ctx = document.getElementById('portfolioChart').getContext('2d');
    if (portfolioChart) portfolioChart.destroy();

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
                        above: 'rgba(63, 185, 80, 0.15)',
                        below: 'rgba(248, 81, 73, 0.15)'
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
            interaction: { mode: 'index', intersect: false },
            plugins: {
                tooltip: { backgroundColor: 'rgba(22, 27, 34, 0.9)', titleColor: '#e6edf3', bodyColor: '#e6edf3', borderColor: 'rgba(255,255,255,0.1)', borderWidth: 1 },
                legend: { labels: { color: '#8b949e' } }
            },
            scales: {
                x: { grid: { color: 'rgba(255, 255, 255, 0.05)' }, ticks: { color: '#8b949e', maxTicksLimit: 10 } },
                y: { grid: { color: 'rgba(255, 255, 255, 0.05)' }, ticks: { color: '#8b949e' } }
            }
        }
    });
}

// --- LÓGICA ESCÁNER ---
async function runScanner(ticker) {
    const periodo = scanPeriodo.value;
    const porcentaje = scanPorcentaje.value;

    const response = await fetch(`/api/scan_surges?ticker=${ticker}&periodo=${periodo}&porcentaje=${porcentaje}`);
    if (!response.ok) {
        const data = await response.json();
        throw new Error(data.detail || "Error en el Escáner de Subidas.");
    }

    const data = await response.json();

    // Update total
    scanTotal.textContent = data.total_ocurrencias;

    // Fill Table
    scanTableBody.innerHTML = '';

    if (data.eventos.length === 0) {
        scanTableBody.innerHTML = `<tr><td colspan="3" class="empty-state">No se encontraron subidas del ${porcentaje}% para este periodo.</td></tr>`;
        return;
    }

    data.eventos.forEach(evento => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${evento.fecha}</td>
            <td>${evento.precio.toFixed(2)}</td>
            <td class="up-trend">+${evento.porcentaje.toFixed(2)}%</td>
        `;
        scanTableBody.appendChild(tr);
    });
}

// --- UTILS ---
function setLoadingState(isLoading) {
    btnAction.disabled = isLoading;
    if (isLoading) {
        btnText.style.display = 'none';
        btnLoader.style.display = 'block';
    } else {
        btnText.style.display = 'block';
        btnLoader.style.display = 'none';
    }
}

function showError(msg) {
    errorMessage.textContent = `❌ ${msg}`;
    errorMessage.style.display = 'block';
    if (activeTab === 'simulator-section') {
        valFinal.textContent = "-- €";
        valRentabilidad.textContent = "-- %";
    }
}

