import React, { useEffect } from 'react'
import * as echarts from "echarts";

const midLowerStyle: React.CSSProperties = {
  display: 'flex',
  height: "64%",
  textAlign: 'center',
  alignItems: 'center',
  justifyContent: 'center',
}

export default function MidLower() {
  useEffect(() => {
    fetch('/ability').then(res => res.json()).then(data => {
      const colorList = [
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
      const series = [
        {
          type: "bar",
          barWidth: 16,
          itemStyle: {
            color: (params: any) => {
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
      const options = {
        title: {
          text: "Top 10 Abilities of Pokemon Count",
          left: 'center',
          textStyle: {
            fontSize: 16,
            color: "#fff",
          }
        },
        dataset: {
          source: [],
        },
        xAxis: {
          type: "value",
          axisLabel: {
            show: true,
            color: 'white',
            fontSize: 12,
          },
        },
        yAxis: {
          type: "category",
          axisLabel: {
            show: true,
            color: 'white',
            fontSize: 12,
          },
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
      };
      options.dataset.source = data;
      let node = document.getElementById('ml');
      let myChart = echarts.init(node as any);
      myChart.setOption(options);
    })
  }, [])
  return (
    <div id='ml' style={midLowerStyle} />
  )
}
