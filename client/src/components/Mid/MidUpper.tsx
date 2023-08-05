import React, { useEffect, useState } from 'react'
import { Col, Row } from 'antd';

const midUpperRowStyle: React.CSSProperties = {
    display: 'flex',
    height: "36%",
    top: "0%",
    textAlign: 'center',
    alignItems: 'center',
    justifyContent: 'center',
}

const midUpperColStyle: React.CSSProperties = {
    display: 'flex',
    flexDirection: 'column',
    height: "100%",
    textAlign: 'center',
    alignItems: 'center',
    justifyContent: 'center',
}

const midUUStyle: React.CSSProperties = {
    display: 'flex',
    height: "60%",
    top: "0",
    width: "100%",
    textAlign: 'center',
    alignItems: 'center',
    justifyContent: 'center',
    color: 'gold',
    fontWeight: 'bold',
    fontSize: 'calc(100vw * 44 / 1500)',
}

const midULStyle: React.CSSProperties = {
    display: 'flex',
    height: "40%",
    top: "60%",
    width: "100%",
    textAlign: 'center',
    justifyContent: 'center',
    color: 'white',
    fontFamily: 'Times New Roman',
    fontWeight: 'bold',
    fontSize: 'calc(100vw * 28 / 1500)',
}


export default function MidUpper() {
    const [pokemon, setPokemon] = useState(0);
    const [ability, setAbility] = useState(0);
    const [skill, setSkill] = useState(0);
    const [generation, setGeneration] = useState(0);
    useEffect(() => {
        fetch('/num').then(res => res.json()).then(data => {
            setPokemon(data.pokemon);
            setAbility(data.ability);
            setSkill(data.skill);
            setGeneration(data.gen);
        });
    }, []);
    return (
        <Row style={midUpperRowStyle}>
            <Col span={6} style={midUpperColStyle}>
                <div style={midUUStyle}>{pokemon}</div>
                <div style={midULStyle}>Pokemon</div>
            </Col>
            <Col span={6} style={midUpperColStyle}>
                <div style={midUUStyle}>{ability}</div>
                <div style={midULStyle}>Ability</div>
            </Col>
            <Col span={6} style={midUpperColStyle}>
                <div style={midUUStyle}>{skill}</div>
                <div style={midULStyle}>Skill</div>
            </Col>
            <Col span={6} style={midUpperColStyle}>
                <div style={midUUStyle}>{generation}</div>
                <div style={midULStyle}>Generation</div>
            </Col>
        </Row>
    )
}
