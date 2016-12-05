$(document).ready(function() {
	$(weatherchart_id).highcharts({
		title: {text: 'Vuoden keskilämpötila', x: -50},
		xAxis: {categories: ['Tammikuu', 'Helmikuu', 'Maaliskuu', 'Huhtikuu', 'Toukokuu', 'Kesäkuu', 'Heinäkuu', 'Elokuu', 'Syyskuu', 'Lokakuu', 'Marraskuu', 'Joulukuu'] },
		yAxis: weatheryAxis,
        legend: weatherlegend,
		series: weatherseries,
        tooltip: weathertooltip,
        chart: weatherchart
	});
});