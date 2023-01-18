let ec_left2 = echarts.init(document.getElementById('l2'), 'dark');

let ec_left2_options = {
    title: {
        text: 'Skill And Ability Count For Each Generation',
        left: 'left'
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'line',
            lineStyle: {
                color: '#7171C6'
            }
        }
    },
    legend: {
        data: ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
        left: 'right'
    },
    grid: {
        left: '6%',
        right: '4%',
        bottom: '6%',
        top: 50,
        containLabel: true
    },
    xAxis: [{
        type: 'category',
        data: []
    }],
    yAxis: {
        type: 'value',
        axisLine: {
            show: true
        },
        axisLabel: {
            show: true,
            color: 'white',
            fontSize: 12,
            formatter: function (value) {
                if (value >= 1000) {
                    value = value / 1000 + 'k';
                }
                return value;
            }
        },
        splitLine: {
            show: true,
            lineStyle: {
                color: '#172738',
                width: 1,
                type: 'solid'
            }
        }
    },
    series: [
        {
            name: 'Pokemon',
            data: [],
            type: 'line',
            smooth: true
        },
        {
            name: 'Skill',
            data: [],
            type: 'line',
            smooth: true
        },
        {
            name: 'Ability',
            data: [],
            type: 'line',
            smooth: true
        }
    ]
}

ec_left2.setOption(ec_left2_options);