import time
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from analysis import PokemonInfo, Skill, Ability


def get_time():
    return time.strftime("%Y/%m/%d %X")


def connect(user, password, db, host='localhost', port=5432):
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)
    return create_engine(url, echo=True, future=True, pool_size=5, pool_recycle=3600)


def get_pokemon_num():
    engine = connect('test', '123456', 'pokemon')
    session = Session(engine)
    num = session.query(func.count('*')).select_from(PokemonInfo).scalar()
    return num


def get_skill_num():
    engine = connect('test', '123456', 'pokemon')
    session = Session(engine)
    num = session.query(func.count('*')).select_from(Skill).scalar()
    return num


def get_ability_num():
    engine = connect('test', '123456', 'pokemon')
    session = Session(engine)
    num = session.query(func.count('*')).select_from(Ability).scalar()
    return num
