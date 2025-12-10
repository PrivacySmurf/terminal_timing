(function () {
  const chartContainer = document.getElementById('chart');
  const statusEl = document.getElementById('status');

  if (!chartContainer || !statusEl) {
    // Nothing we can do, but avoid throwing
    return;
  }

  function setStatus(msg, isError) {
    statusEl.textContent = msg;
    statusEl.classList.toggle('error', !!isError);
  }

  function toSeriesData(entries) {
    return entries
      .filter((p) => typeof p.time === 'number' && typeof p.value === 'number')
      .map((p) => ({ time: p.time, value: p.value }));
  }

  async function loadChartData() {
    try {
      setStatus('Loading chart data…', false);
      const res = await fetch('./chart-data.json', { cache: 'no-cache' });
      if (!res.ok) {
        throw new Error(`HTTP ${res.status}`);
      }
      const data = await res.json();

      if (!data || !Array.isArray(data.btcPrice) || !Array.isArray(data.phaseScore)) {
        throw new Error('Invalid chart-data.json schema');
      }

      renderChart(data);
      const lastUpdated = data.lastUpdated || 'unknown time';
      setStatus(`Chart loaded (lastUpdated: ${lastUpdated}, dataQuality: ${data.dataQuality || 'n/a'})`, false);
    } catch (err) {
      console.error('Failed to load chart-data.json', err);
      setStatus('Chart data is currently unavailable. Please try again later.', true);
    }
  }

  function renderChart(data) {
    const priceData = toSeriesData(data.btcPrice || []);
    const phaseData = toSeriesData(data.phaseScore || []);

    if (priceData.length === 0 || phaseData.length === 0) {
      throw new Error('Empty series in chart-data.json');
    }

    // Align to overlapping time range
    const minTime = Math.max(priceData[0].time, phaseData[0].time);
    const maxTime = Math.min(priceData[priceData.length - 1].time, phaseData[phaseData.length - 1].time);

    const clippedPrice = priceData.filter((p) => p.time >= minTime && p.time <= maxTime);
    const clippedPhase = phaseData.filter((p) => p.time >= minTime && p.time <= maxTime);

    // Create chart
    const chart = LightweightCharts.createChart(chartContainer, {
      layout: {
        background: { color: '#020617' },
        textColor: '#e5e7eb',
      },
      rightPriceScale: {
        borderVisible: false,
      },
      leftPriceScale: {
        visible: true,
        borderVisible: false,
      },
      timeScale: {
        borderVisible: false,
      },
      grid: {
        vertLines: { color: '#111827' },
        horzLines: { color: '#111827' },
      },
    });

    const priceSeries = chart.addAreaSeries({
      priceScaleId: 'right',
      lineColor: '#38bdf8',
      topColor: 'rgba(56, 189, 248, 0.4)',
      bottomColor: 'rgba(56, 189, 248, 0.05)',
    });

    const phaseScaleId = 'left';
    const phaseSeries = chart.addLineSeries({
      priceScaleId: phaseScaleId,
      color: '#f97316',
      lineWidth: 2,
    });

    priceSeries.setData(clippedPrice);
    phaseSeries.setData(clippedPhase);

    chart.timeScale().fitContent();
  }

  loadChartData();
})();
