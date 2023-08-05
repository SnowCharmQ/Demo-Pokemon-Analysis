import React from 'react'
import { Col, Layout, Row } from 'antd';
import '../styles/Analysis.css'
import Title from '../components/Header/Title';
import Time from '../components/Header/Time';
import LeftUpper from '../components/Left/LeftUpper';
import LeftLower from '../components/Left/LeftLower';

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

const leftUpperStyle: React.CSSProperties = {
  display: 'flex',
  height: "50%",
  top: "0%",
  textAlign: 'center',
  alignItems: 'center',
  justifyContent: 'center',
}

const leftLowerStyle: React.CSSProperties = {
  display: 'flex',
  height: "50%",
  top: "50%",
  textAlign: 'center',
  alignItems: 'center',
  justifyContent: 'center',
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
        <Row style={contentRowStyle}>
          <Col span={8}> 
            <div style={leftUpperStyle}>
              <LeftUpper />
            </div>
            <div style={leftLowerStyle}>
              <LeftLower />
            </div>
          </Col>
          <Col span={8} />
          <Col span={8} />
        </Row>
      </Content>
    </Layout>
  )
}
