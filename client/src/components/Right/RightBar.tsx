import { Image, Row, Col } from 'antd'
import Search from 'antd/es/input/Search'
import React, { useState } from 'react'

interface ColorMap {
    [key: string]: string
}

const typeColorMap: ColorMap = {
    'normal': '#9fa19f',
    'flying': '#81b9ef',
    'fire': '#e62829',
    'psychic': '#ef4179',
    'water': '#2980ef',
    'bug': '#91a119',
    'electric': '#fac000',
    'rock': '#afa981',
    'grass': '#3fa129',
    'ghost': '#704170',
    'ice': '#3fd8ff',
    'dragon': '#5060e1',
    'fighting': '#ff8000',
    'dark': '#50413f',
    'poison': '#9141cb',
    'steel': '#60a1b8',
    'ground': '#915121',
    'fairy': '#ef70ef'
}

const fallbackUrl = "data:image/png;base64,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"

const rightBarStyle: React.CSSProperties = {
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    width: '100%',
    height: '100%',
}

const searchStyle: React.CSSProperties = {
    width: '100%',
    height: '5%',
    top: '1%',
    justifyContent: 'center',
    alignItems: 'center',
    textAlign: 'center',
}

const imageTypeStyle: React.CSSProperties = {
    display: 'flex',
    width: '100%',
    height: '36%',
    top: '3%',
}

const imageStyle: React.CSSProperties = {
    display: 'flex',
    width: '76%',
    height: '100%',
    justifyContent: 'center',
    alignItems: 'center',
    textAlign: 'center',
}

const typeStyle: React.CSSProperties = {
    display: 'flex',
    flexDirection: 'column',
    width: '24%',
    height: '100%',
    justifyContent: 'center',
}

const pokeinfoStyle: React.CSSProperties = {
    display: 'flex',
    width: '100%',
    height: '10%',
    top: '44%',
}

const pokeinfoSubStyle: React.CSSProperties = {
    display: 'flex',
    width: '80%',
    height: '100%',
    alignItems: 'center',
    textAlign: 'center',
    justifyContent: 'center',
    lineHeight: '8%',
    fontFamily: 'Times New Roman',
    fontWeight: 'bold',
    fontSize: '1.5vw',
    color: 'gold'
}

const pokeCardStyle: React.CSSProperties = {
    display: 'flex',
    width: '84%',
    height: '36%',
    marginTop: '-2%',
    backgroundColor: '#30a7d7',
    borderRadius: '10px',
}

const cardinfoStyle: React.CSSProperties = {
    display: 'flex',
    flexDirection: 'column',
    width: '100%',
    height: '33.3%',
    justifyContent: 'center',
    alignItems: 'center',
    textAlign: 'center',
}

const cardinfoUpperStyle: React.CSSProperties = {
    display: 'flex',
    width: '100%',
    height: '50%',
    justifyContent: 'center',
    alignItems: 'center',
    textAlign: 'center',
    fontFamily: 'Flexo-Medium',
    fontSize: '1.1vw',
    color: 'white',
    fontWeight: 'bold',
}

const cardinfoLowerStyle: React.CSSProperties = {
    display: 'flex',
    width: '100%',
    height: '50%',
    justifyContent: 'center',
    alignItems: 'center',
    textAlign: 'center',
    fontFamily: 'Flexo-Medium',
    fontSize: '1.22vw',
}

const statTableStyle: React.CSSProperties = {
    display: 'flex',
    width: '100%',
    height: '14%',
    justifyContent: 'center',
    alignItems: 'center',
    textAlign: 'center',
}

const statColStyle: React.CSSProperties = {
    display: 'flex',
    flexDirection: 'column',
    height: '100%',
    justifyContent: 'center',
    alignItems: 'center',
    textAlign: 'center',
}

const statUpperStyle: React.CSSProperties = {
    display: 'flex',
    width: '100%',
    height: '50%',
    justifyContent: 'center',
    alignItems: 'center',
    textAlign: 'center',
    border: '1.3px #00fffd solid',
    fontFamily: 'Flexo-Medium',
    color: 'white',
}

const statLowerStyle: React.CSSProperties = {
    display: 'flex',
    width: '100%',
    height: '50%',
    justifyContent: 'center',
    alignItems: 'center',
    textAlign: 'center',
    border: '1.3px #00fffd solid',
    fontFamily: 'Flexo-Medium',
    fontWeight: 'bold',
    color: 'gold',
}

export default function RightBar() {
    const [displayMain, setDisplayMain] = useState('none');
    const [type1, setType1] = useState('');
    const [type2, setType2] = useState('');
    const [color1, setColor1] = useState('#000');
    const [color2, setColor2] = useState('#000');
    const [isType1, setIsType1] = useState('none');
    const [isType2, setIsType2] = useState('none');
    const [srcUrl, setSrcUrl] = useState(fallbackUrl);
    const [name, setName] = useState('');
    const [label, setLabel] = useState('');
    const [id, setId] = useState('');
    const [species, setSpecies] = useState('');
    const [abilities, setAbilities] = useState('');
    const [height, setHeight] = useState('');
    const [weight, setWeight] = useState('');
    const [gender, setGender] = useState('');
    const [eggs, setEggs] = useState('');
    const [hp, setHp] = useState('');
    const [atk, setAtk] = useState('');
    const [def, setDef] = useState('');
    const [spatk, setSpatk] = useState('');
    const [spdef, setSpdef] = useState('');
    const [spd, setSpd] = useState('');
    const [total, setTotal] = useState('');
    let typeStyleSub1: React.CSSProperties = {
        display: isType1,
        width: '82%',
        height: '12%',
        justifyContent: 'center',
        alignItems: 'center',
        textAlign: 'center',
        fontFamily: 'Times New Roman',
        fontWeight: 'bold',
        fontSize: '1.2vw',
        backgroundColor: color1,
    }
    let typeStyleSub2: React.CSSProperties = {
        display: isType2,
        width: '82%',
        height: '12%',
        justifyContent: 'center',
        alignItems: 'center',
        textAlign: 'center',
        marginTop: '36%',
        fontFamily: 'Times New Roman',
        fontWeight: 'bold',
        fontSize: '1.2vw',
        backgroundColor: color2,
    }
    let mainStyle: React.CSSProperties = {
        display: displayMain,
        flexDirection: 'column',
        height: '93%',
        width: '100%',
        top: '7%',
        alignItems: 'center',
        textAlign: 'center',
    }
    const formatId = (id: string) => {
        if (id === '') return '';
        let res = '';
        for (let i = 0; i < 4 - id.length; i++) {
            res += '0';
        }
        return '#' + res + id;
    }
    const updateDetail = (data: any) => {
        if (data.code === 200) {
            setDisplayMain('flex');
            setName(data.name);
            setLabel(data.label);
            setId(data.id);
            setSpecies(data.species);
            setAbilities(data.abilities);
            setHeight(data.height);
            setWeight(data.weight);
            setGender(data.gender);
            let dataEggs = data.eggs.replace(/'/g, "")
                .replace(/"/g, '').replace('[', '').replace(']', '');
            setEggs(dataEggs);
            setSrcUrl(data.img);
            setType1(data.type1);
            setColor1(typeColorMap[(data.type1 as string).toLowerCase()]);
            setIsType1('flex');
            if (data.type2 !== null) {
                setType2(data.type2);
                setIsType2('flex');
                setColor2(typeColorMap[(data.type2 as string).toLowerCase()]);
            } else {
                setIsType2('none');
            }
            setHp(data.hp);
            setAtk(data.attack);
            setDef(data.defense);
            setSpatk(data.sp_attack);
            setSpdef(data.sp_defense);
            setSpd(data.speed);
            setTotal(data.total);
        }
    }
    const onsearch = (value: string) => {
        fetch(`http://localhost:5000/detail`, {
            method: 'POST',
            mode: 'cors',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                msg: value
            })
        }).then(res => res.json())
            .then(data => {
                updateDetail(data);
            })
    }
    return (
        <div style={rightBarStyle}>
            <div style={{ height: '1%', width: '100%' }} />
            <div style={searchStyle}>
                <Search placeholder='Input Here' allowClear
                    style={{ width: '70%' }} onSearch={onsearch} />
            </div>
            <div style={mainStyle}>
                <div style={{ height: '3%', width: '100%' }} />
                <div style={imageTypeStyle}>
                    <div style={imageStyle}>
                        <Image
                            width={300}
                            height={300}
                            src={srcUrl}
                            fallback={fallbackUrl}
                        />
                    </div>
                    <div style={typeStyle}>
                        <div style={typeStyleSub1}>{type1}</div>
                        <div style={typeStyleSub2}>{type2}</div>
                    </div>
                </div>
                <div style={pokeinfoStyle}>
                    <div style={pokeinfoSubStyle}>
                        {name} ({label}) &ensp; {formatId(id.toString())}
                    </div>
                </div>
                <div style={pokeCardStyle}>
                    <Row style={{ width: '100%', height: '100%' }}>
                        <Col span={12} style={{ height: '100%' }}>
                            <div style={cardinfoStyle}>
                                <div style={cardinfoUpperStyle}>Species</div>
                                <div style={cardinfoLowerStyle}>{species}</div>
                            </div>
                            <div style={cardinfoStyle}>
                                <div style={cardinfoUpperStyle}>Height</div>
                                <div style={cardinfoLowerStyle}>{height}</div>
                            </div>
                            <div style={cardinfoStyle}>
                                <div style={cardinfoUpperStyle}>Gender</div>
                                <div style={cardinfoLowerStyle}>{gender}</div>
                            </div>
                        </Col>
                        <Col span={12} style={{ height: '100%' }}>
                            <div style={cardinfoStyle}>
                                <div style={cardinfoUpperStyle}>Abilities</div>
                                <div style={cardinfoLowerStyle}>{abilities}</div>
                            </div>
                            <div style={cardinfoStyle}>
                                <div style={cardinfoUpperStyle}>Weight</div>
                                <div style={cardinfoLowerStyle}>{weight}</div>
                            </div>
                            <div style={cardinfoStyle}>
                                <div style={cardinfoUpperStyle}>Eggs</div>
                                <div style={cardinfoLowerStyle}>{eggs}</div>
                            </div>
                        </Col>
                    </Row>
                </div>
                <div style={{ width: '100%', height: '1.5%' }} />
                <div style={statTableStyle}>
                    <Row style={{ width: '100%', height: '100%' }}>
                        <Col span={1} style={statColStyle}/>
                        <Col span={3} style={statColStyle}>
                            <div style={statUpperStyle}>HP</div>
                            <div style={statLowerStyle}>{hp}</div>
                        </Col>
                        <Col span={3} style={statColStyle}>
                            <div style={statUpperStyle}>Attack</div>
                            <div style={statLowerStyle}>{atk}</div>
                        </Col>
                        <Col span={3} style={statColStyle}>
                            <div style={statUpperStyle}>Defense</div>
                            <div style={statLowerStyle}>{def}</div>
                        </Col>
                        <Col span={3} style={statColStyle}>
                            <div style={statUpperStyle}>Sp. Atk</div>
                            <div style={statLowerStyle}>{spatk}</div>
                        </Col>
                        <Col span={3} style={statColStyle}>
                            <div style={statUpperStyle}>Sp. Def</div>
                            <div style={statLowerStyle}>{spdef}</div>
                        </Col>
                        <Col span={3} style={statColStyle}>
                            <div style={statUpperStyle}>Speed</div>
                            <div style={statLowerStyle}>{spd}</div>
                        </Col>
                        <Col span={4} style={statColStyle}>
                            <div style={statUpperStyle}>Total</div>
                            <div style={statLowerStyle}>{total}</div>
                        </Col>
                        <Col span={1} style={statColStyle}/>
                    </Row>
                </div>
            </div>
        </div>
    )
}
