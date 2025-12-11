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

      // Support both new 'lsd' field and legacy 'phaseScore'
      const lsdData = data.lsd || data.phaseScore;
      if (!data || !Array.isArray(data.btcPrice) || !Array.isArray(lsdData)) {
        throw new Error('Invalid chart-data.json schema');
      }
      data.lsd = lsdData;

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
    const phaseData = toSeriesData(data.lsd || data.phaseScore || []);

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
        visible: true,
        borderVisible: false,
        scaleMargins: { top: 0.1, bottom: 0.1 },
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

    // BTC Price on LEFT (orange line, no gradient)
    const priceSeries = chart.addLineSeries({
      priceScaleId: 'left',
      color: '#f97316', // orange
      lineWidth: 2,
      priceFormat: { type: 'price', precision: 0, minMove: 1 },
    });

    // LSD on RIGHT (fuchsia, fixed 0-100 scale)
    const lsdSeries = chart.addLineSeries({
      priceScaleId: 'right',
      color: '#d946ef', // fuchsia
      lineWidth: 2,
      priceFormat: { type: 'price', precision: 1, minMove: 0.1 },
    });

    // Configure right scale for LSD (0-100 range)
    chart.priceScale('right').applyOptions({
      scaleMargins: { top: 0.05, bottom: 0.05 },
      autoScale: false,
    });

    priceSeries.setData(clippedPrice);
    lsdSeries.setData(clippedPhase);

    // Add zone markers on LSD scale
    // Retention zone (0-20) - green
    lsdSeries.createPriceLine({
      price: 20,
      color: 'rgba(34, 197, 94, 0.6)',
      lineWidth: 1,
      lineStyle: 2, // dashed
      axisLabelVisible: true,
      title: '',
    });

    // Distribution zone (80-100) - red  
    lsdSeries.createPriceLine({
      price: 80,
      color: 'rgba(239, 68, 68, 0.6)',
      lineWidth: 1,
      lineStyle: 2, // dashed
      axisLabelVisible: true,
      title: '',
    });

    // Add zone watermarks as overlay divs
    const chartRect = chartContainer.getBoundingClientRect();
    
    // Create retention zone overlay (bottom)
    const retentionZone = document.createElement('div');
    retentionZone.style.cssText = `
      position: absolute;
      bottom: 0;
      left: 0;
      right: 60px;
      height: 20%;
      background: linear-gradient(to top, rgba(34, 197, 94, 0.15), transparent);
      pointer-events: none;
      display: flex;
      align-items: center;
      justify-content: center;
    `;
    retentionZone.innerHTML = '<span style="color: rgba(34, 197, 94, 0.4); font-size: 24px; font-weight: bold; text-transform: uppercase;">Retention</span>';
    chartContainer.style.position = 'relative';
    chartContainer.appendChild(retentionZone);

    // Create distribution zone overlay (top)
    const distributionZone = document.createElement('div');
    distributionZone.style.cssText = `
      position: absolute;
      top: 0;
      left: 0;
      right: 60px;
      height: 20%;
      background: linear-gradient(to bottom, rgba(239, 68, 68, 0.15), transparent);
      pointer-events: none;
      display: flex;
      align-items: center;
      justify-content: center;
    `;
    distributionZone.innerHTML = '<span style="color: rgba(239, 68, 68, 0.4); font-size: 24px; font-weight: bold; text-transform: uppercase;">Distribution</span>';
    chartContainer.appendChild(distributionZone);

    // Set visible range to last 100 data points by default
    const visibleBars = 100;
    if (clippedPrice.length > visibleBars) {
      const fromTime = clippedPrice[clippedPrice.length - visibleBars].time;
      const toTime = clippedPrice[clippedPrice.length - 1].time;
      chart.timeScale().setVisibleRange({ from: fromTime, to: toTime });
    } else {
      chart.timeScale().fitContent();
    }
  }

  loadChartData();
})();
