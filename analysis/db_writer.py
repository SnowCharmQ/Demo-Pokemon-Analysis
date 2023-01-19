import pandas as pd
from sqlalchemy import create_engine, Integer, Column, VARCHAR, UniqueConstraint
from sqlalchemy.orm import Session, declarative_base

Base = declarative_base()


def connect(user, password, db, host='localhost', port=5432):
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)
    return create_engine(url, echo=True, future=True, pool_size=5, pool_recycle=3600)


class PokemonInfo(Base):
    __tablename__ = "pokemon_info"
    idx = Column(Integer, autoincrement=True, primary_key=True)
    id = Column(Integer)
    href = Column(VARCHAR(100))
    name = Column(VARCHAR(100))
    detail = Column(VARCHAR(100))
    type1 = Column(VARCHAR(100))
    type2 = Column(VARCHAR(100))
    gen = Column(VARCHAR(10))


class Skill(Base):
    __tablename__ = "skill"
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(100))
    type = Column(VARCHAR(100))
    category = Column(VARCHAR(100))
    pp = Column(VARCHAR(100))
    power = Column(VARCHAR(100))
    accuracy = Column(Integer)
    gen = Column(VARCHAR(10))


class Ability(Base):
    __tablename__ = "ability"
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(100))
    description = Column(VARCHAR(1000))
    gen = Column(VARCHAR(10))


class PokemonAbility(Base):
    __tablename__ = "pokemon_ability"
    idx = Column(Integer, autoincrement=True, primary_key=True)
    id = Column(Integer)
    name = Column(VARCHAR(100))
    detail = Column(VARCHAR(100))
    ability1 = Column(VARCHAR(100))
    ability2 = Column(VARCHAR(100))
    hide_ability = Column(VARCHAR(100))


def save_pokemon_info():
    session = Session(engine)
    objects = []
    df = pd.read_csv("../data/pokemon.csv")
    for data in df.itertuples():
        data_id = int(data.id)
        if data_id <= 151:
            gen = 'I'
        elif 151 < data_id <= 251:
            gen = 'II'
        elif 251 < data_id <= 386:
            gen = 'III'
        elif 386 < data_id <= 493:
            gen = 'IV'
        elif 493 < data_id <= 649:
            gen = 'V'
        elif 649 < data_id <= 721:
            gen = 'VI'
        elif 721 < data_id <= 809:
            gen = 'VII'
        elif 809 < data_id <= 905:
            gen = 'VIII'
        else:
            gen = 'IX'
        type1 = data.type1
        type2 = data.type2
        detail = data.detail
        type1 = type1 if type(type1) == str else ''
        type2 = type2 if type(type2) == str else ''
        detail = detail if type(detail) == str else ''
        obj = PokemonInfo(id=data_id, href=data.href, name=data.name,
                          detail=detail, type1=type1, type2=type2, gen=gen)
        objects.append(obj)
    session.bulk_save_objects(objects)
    session.commit()


def save_skill():
    session = Session(engine)
    objects = []
    df = pd.read_csv("../data/skill.csv")
    for data in df.itertuples():
        data_id, data_name, data_type, data_category, data_pp, data_power, data_accuracy, data_gen = \
            data.id, data.name, data.type, data.category, data.pp, data.power, data.accuracy, data.gen
        data_pp = data_pp.replace("*", "")
        data_power = data_power.replace("*", "")
        data_power = None if '—' in data_power else data_power
        data_accuracy = data_accuracy.replace("*", "").replace("%", "")
        data_accuracy = None if '—' in data_accuracy else data_accuracy
        data_gen = data_gen.replace("*", "")
        obj = Skill(id=data_id, name=data_name, type=data_type, category=data_category,
                    pp=data_pp, power=data_power, accuracy=data_accuracy, gen=data_gen)
        objects.append(obj)
    session.bulk_save_objects(objects)
    session.commit()


def save_ability():
    session = Session(engine)
    objects = []
    df = pd.read_csv("../data/ability.csv")
    for data in df.itertuples():
        obj = Ability(id=data.id, name=data.name,
                      description=data.description,
                      gen=data.gen)
        objects.append(obj)
    session.bulk_save_objects(objects)
    session.commit()


def save_pokemon_ability():
    session = Session(engine)
    objects = []
    df = pd.read_csv("../data/pokemon_ability.csv")
    for data in df.itertuples():
        ability1 = data.ability1
        ability2 = data.ability2
        hide_ability = data.hide_ability
        ability1 = ability1.replace("*", "") if type(ability1) == str else ''
        ability2 = ability2.replace("*", "") if type(ability2) == str else ''
        hide_ability = hide_ability.replace("*", "") if type(hide_ability) == str else ''
        obj = PokemonAbility(id=data.id, name=data.name, detail=data.detail,
                             ability1=ability1, ability2=ability2,
                             hide_ability=hide_ability)
        objects.append(obj)
    session.bulk_save_objects(objects)
    session.commit()


if __name__ == "__main__":
    engine = connect('test', '123456', 'pokemon')
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    save_pokemon_info()
    save_skill()
    save_ability()
    save_pokemon_ability()
