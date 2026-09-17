<script>
  import { onMount } from 'svelte'
  import * as echarts from 'echarts'

  let pieEl
  let barEl

  onMount(async () => {
    const res = await fetch('/data')
    const data = await res.json()

    echarts.init(pieEl).setOption({
      title: { text: 'Piechart' },
      tooltip: {},
      series: [{
        type: 'pie',
        data: data.piechart.labels.map((name, i) => ({
          name,
          value: data.piechart.values[i],
        })),
      }],
    })

    echarts.init(barEl).setOption({
      title: { text: 'Barplot' },
      tooltip: {},
      xAxis: { type: 'category', data: data.barplot.categories },
      yAxis: { type: 'value' },
      series: [{ type: 'bar', data: data.barplot.values }],
    })
  })
</script>

<main>
  <div bind:this={pieEl} style="width: 100%; height: 400px;"></div>
  <div bind:this={barEl} style="width: 100%; height: 400px;"></div>
</main>
