let ec_left1 = echarts.init(document.getElementById('l1'), 'dark');

let ec_left1_options = {
    title: {
        text: 'Pokemon Count For Each Type',
        left: 'center'
    },
    tooltip: {
        trigger: 'item'
    },
    legend: {
        x: 'center',
        y: 'bottom'
    },
    series: [
        {
            name: 'Access From',
            type: 'pie',
            radius: '50%',
            center: ['50%', '42%'],
            data: [],
            emphasis: {
                itemStyle: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ]
};

ec_left1.setOption(ec_left1_options);