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


def get_pokemon_gen():
    engine = connect('test', '123456', 'pokemon')
    session = Session(engine)
    pokemons = session.query(PokemonInfo.gen, func.count(PokemonInfo.gen)).group_by(PokemonInfo.gen).all()
    pokemon_dict = {}
    for pokemon in pokemons:
        pokemon_dict[pokemon[0]] = pokemon[1]
    return pokemon_dict


def get_skill_gen():
    engine = connect('test', '123456', 'pokemon')
    session = Session(engine)
    skills = session.query(Skill.gen, func.count(Skill.gen)).group_by(Skill.gen).all()
    skill_dict = {}
    for skill in skills:
        skill_dict[skill[0]] = skill[1]
    return skill_dict


def get_ability_gen():
    engine = connect('test', '123456', 'pokemon')
    session = Session(engine)
    abilities = session.query(Ability.gen, func.count(Ability.gen)).group_by(Ability.gen).all()
    ability_dict = {}
    for ability in abilities:
        ability_dict[ability[0]] = ability[1]
    return ability_dict


def get_pokemon_type():
    engine = connect('test', '123456', 'pokemon')
    session = Session(engine)
    pokemons = session.query(PokemonInfo).all()
    pokemon_type = {}
    for pokemon in pokemons:
        type1 = pokemon.type1
        type2 = pokemon.type2
        if type1 == 'GrassGroundSteel' or type2 == 'GrassGroundSteel':
            pokemon_type['Grass'] = pokemon_type['Grass'] + 1
            pokemon_type['Ground'] = pokemon_type['Ground'] + 1
            pokemon_type['Steel'] = pokemon_type['Steel'] + 1
            continue
        if type1 == 'FireElectricPsychicGhost' or type2 == 'FireElectricPsychicGhost':
            pokemon_type['Fire'] = pokemon_type['Fire'] + 1
            pokemon_type['Electric'] = pokemon_type['Electric'] + 1
            pokemon_type['Psychic'] = pokemon_type['Psychic'] + 1
            pokemon_type['Ghost'] = pokemon_type['Ghost'] + 1
            continue
        if type1 is not None and type1 in pokemon_type:
            pokemon_type[type1] = pokemon_type[type1] + 1
        elif type1 is not None and type1 not in pokemon_type:
            pokemon_type[type1] = 1
        if type2 is not None and type2 in pokemon_type:
            pokemon_type[type2] = pokemon_type[type2] + 1
        elif type2 is not None and type2 not in pokemon_type:
            pokemon_type[type2] = 1
    return pokemon_type
