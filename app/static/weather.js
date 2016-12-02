$(document).ready(function() {
	$(weatherchart_id).highcharts({
		title: weathertitle,
		xAxis: weatherxAxis,
		yAxis: weatheryAxis,
        legend: weatherlegend,
		series: weatherseries,
        tooltip: weathertooltip,
        chart: weatherchart
	});
});