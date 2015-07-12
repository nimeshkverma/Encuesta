function load_pie(element,data,title) {
    console.log(data)
    $(element).highcharts({
            chart: {
             backgroundColor: '#4f5762',
                type: 'pie',
                options3d: {
                    enabled: true,
                    alpha: 45,
                    beta: 0
                }
            },
            title: {
                text: question,
                style: {
                    color: 'white'
                }
            },
            tooltip: {
                pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
            },
            plotOptions: {
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    depth: 35,
                    dataLabels: {
                        enabled: true,
                        format: '{point.name}',
                        style: {
                         color: 'white'
                     }
                    }
                }
            },
            series: [{
                type: 'pie',
                name: 'Vote Percent',
                data: data
            }]
        });
}