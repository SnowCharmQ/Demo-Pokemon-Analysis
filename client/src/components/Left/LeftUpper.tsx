import { useEffect } from 'react'
import * as echarts from "echarts";
import '../../styles/Analysis.css'

interface Type {
    value: string
    name: string
}

export default function LeftUpper() {
    useEffect(() => {
        fetch('http://localhost:5000/type', {
            method: 'GET',
            mode: 'cors'
        }).then(res => res.json()).then(data => {
            let result: Type[] = [];
            for (let val in data) {
                let k = val;
                let v = data[val];
                let obj = { value: v.toString(), name: k.toString() };
                result.push(obj);
            }
            let node = document.getElementById('lu');
            const options = {
                title: {
                    text: 'Pokemon Count For Each Type',
                    left: 'center',
                    top: 10,
                    textStyle: {
                        color: '#ccc',
                        fontSize: 16
                    }
                },
                tooltip: {
                    trigger: 'item'
                },
                legend: {
                    x: 'center',
                    y: 'bottom',
                    textStyle: {
                        color: '#ccc'
                    }
                },
                series: [
                    {
                        name: 'Access From',
                        type: 'pie',
                        radius: '50%',
                        center: ['50%', '42%'],
                        data: result as Type[],
                        label: {
                            normal: {
                                textStyle: {
                                    color: '#ccc'
                                }
                            }
                        },
                    }
                ]
            };
            let myChart = echarts.init(node as any);
            myChart.setOption(options as any);
        })
    }, [])
    return (
        <div id="lu" />
    )
}
