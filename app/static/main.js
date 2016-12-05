$(document).ready(function() {
	$(chart_id).highcharts({
		chart: chart,
		title: {text: 'Suomen väestörakenne'},
		xAxis: xAxis,
		yAxis: yAxis,
		series: series,
        plotOptions: plotOptions,
        tooltip: tooltip
	});
});