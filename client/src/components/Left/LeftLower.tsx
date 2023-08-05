import { useEffect } from 'react'
import * as echarts from "echarts";

export default function LeftLower() {
    useEffect(() => {
        fetch('/gen').then(res => res.json()).then(data => {
            const options = {
                title: {
                    text: 'Pokemon, Skill, and Ability Count For Each Generation',
                    left: 'center',
                    top: 10,
                    textStyle: {
                        color: '#ccc',
                        fontSize: 16
                    }
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
                    left: 'right',
                    textStyle: {
                        color: '#ccc'
                    }
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
                    data: [],
                    axisLabel: {
                        show: true,
                        color: 'white',
                        fontSize: 12,
                    },
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
                        smooth: true,
                        color: '#666699'
                    },
                    {
                        name: 'Skill',
                        data: [],
                        type: 'line',
                        smooth: true,
                        color: '#FFFF00'
                    },
                    {
                        name: 'Ability',
                        data: [],
                        type: 'line',
                        smooth: true,
                        color: '#FF0033'
                    }
                ]
            };
            options.xAxis[0].data = data.gen;
            options.series[0].data = data.pokemon;
            options.series[1].data = data.skill;
            options.series[2].data = data.ability;
            let node = document.getElementById('ll');
            let myChart = echarts.init(node as any);
            myChart.setOption(options);
        })
    }, [])
    return (
        <div id='ll' />
    )
}
