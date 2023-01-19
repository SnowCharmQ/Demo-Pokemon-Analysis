let ec_middle = echarts.init(document.getElementById('m2'), 'dark');

let colorList = [
    "#1890ff",
    "#52c41a",
    "#faad14",
    "#f5222d",
    "#1DA57A",
    "#d9d9d9",
    "#54FF9F",
    "#0000CD",
    "#FF6A6A",
    "#FF7F00"
];

let series = [
    {
        type: "bar",
        barWidth: 16,
        itemStyle: {
            color: (params) => {
                return colorList[params.dataIndex];
            },
        },
        dimensions: ["Ability", "Pokemon Count"],
        label: {
            show: true,
            position: "right",
            color: "#333",
            fontSize: 8,
        },
    },
];

let ec_middle_options = {
    title: {
        text: "Top 10 Abilities of Pokemon Count",
        left: 'center',
        textStyle: {
            fontSize: 16
        }
    },
    dataset: {
        source: [],
    },
    xAxis: {
        type: "value"
    },
    yAxis: {
        type: "category"
    },
    series,
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'shadow'
        },
    },
    grid: {
        left: '22%'
    }
}

ec_middle.setOption(ec_middle_options);

