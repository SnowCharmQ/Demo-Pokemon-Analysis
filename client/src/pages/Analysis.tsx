import React from 'react'
import '../styles/Analysis.css'
import { Col, Layout, Row } from 'antd';
import Title from '../components/Title';
import Time from '../components/Time';

const { Header, Content } = Layout;

const headerStyle: React.CSSProperties = {
  textAlign: 'center',
  color: 'white',
  height: '10vh',
  backgroundColor: '#333',
}

const headerRowStyle: React.CSSProperties = {
  height: '100%',
}

const contentStyle: React.CSSProperties = {
  height: '90vh',
  backgroundColor: '#333',
}

const contentRowStyle: React.CSSProperties = {
  height: '100%',
}

const titleStyle: React.CSSProperties = {
  display: 'flex',
  textAlign: 'center',
  alignItems: 'center',
  justifyContent: 'center',
  height: "100%"
}

const timeStyle: React.CSSProperties = {
  display: 'flex',
  height: "30%",
  top: "70%",
  textAlign: 'left',
  alignItems: 'center',
  lineHeight: 'normal',
}

export default function Analysis() {
  return (
    <Layout>
      <Header style={headerStyle}>
        <Row style={headerRowStyle}>
          <Col span={5} />
          <Col span={14} style={titleStyle}>
            <Title />
          </Col>
          <Col span={5} style={timeStyle}>
            <Time />
          </Col>
        </Row>
      </Header>
      <Content style={contentStyle}>
      </Content>
    </Layout>
  )
}
