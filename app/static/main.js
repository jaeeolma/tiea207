$(document).ready(function() {
	$(chart_id).highcharts({
		chart: chart,
		title: {text: 'Suomen väestörakenne'},
		xAxis: xAxis,
		yAxis: {
                title: {
                    text: null
                },
                labels: {
                    formatter: function () {
                        return Math.abs(this.value);
                    }
                }
            },
		series: series,
        plotOptions: plotOptions,
        tooltip: {
                formatter: function () {
                    return '<b>' + this.series.name + ', ' + this.point.category + '</b><br/>' +
                        'Väkiluku: ' + Highcharts.numberFormat(Math.abs(this.point.y), 0);
                }
            }
	});
});