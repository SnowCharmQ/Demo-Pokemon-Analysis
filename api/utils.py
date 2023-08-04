from config import db, PokemonInfo, Skill, Ability, PokemonAbility
from sqlalchemy import func
import warnings
import time
import sys
sys.path.append('..')


warnings.filterwarnings('ignore')


def get_time():
    return time.strftime("%Y/%m/%d %X")


def get_pokemon_num():
    session = db.session
    nums = session.query(func.count(
        '*')).select_from(PokemonInfo).group_by(PokemonInfo.id)
    num = session.query(func.count('*')).select_from(nums).scalar()
    return num


def get_skill_num():
    session = db.session
    num = session.query(func.count('*')).select_from(Skill).scalar()
    return num


def get_ability_num():
    session = db.session
    num = session.query(func.count('*')).select_from(Ability).scalar()
    return num


def get_pokemon_gen():
    session = db.session
    pokemons = session.query(PokemonInfo.gen, func.count(
        PokemonInfo.gen)).group_by(PokemonInfo.gen).all()
    pokemon_dict = {}
    for pokemon in pokemons:
        pokemon_dict[pokemon[0]] = pokemon[1]
    return pokemon_dict


def get_skill_gen():
    session = db.session
    skills = session.query(Skill.gen, func.count(
        Skill.gen)).group_by(Skill.gen).all()
    skill_dict = {}
    for skill in skills:
        skill_dict[skill[0]] = skill[1]
    return skill_dict


def get_ability_gen():
    session = db.session
    abilities = session.query(Ability.gen, func.count(
        Ability.gen)).group_by(Ability.gen).all()
    ability_dict = {}
    for ability in abilities:
        ability_dict[ability[0]] = ability[1]
    return ability_dict


def get_pokemon_type():
    session = db.session
    pokemons = session.query(PokemonInfo).all()
    pokemon_type = {}
    for pokemon in pokemons:
        type1 = pokemon.type1
        type2 = pokemon.type2
        if type1 != '' and type1 in pokemon_type:
            pokemon_type[type1] = pokemon_type[type1] + 1
        elif type1 != '' and type1 not in pokemon_type:
            pokemon_type[type1] = 1
        if type2 != '' and type2 in pokemon_type:
            pokemon_type[type2] = pokemon_type[type2] + 1
        elif type2 != '' and type2 not in pokemon_type:
            pokemon_type[type2] = 1
    return pokemon_type


def get_pokemon_ability():
    session = db.session
    pas = session.query(PokemonAbility).all()
    pokemon_ability = {}
    for pa in pas:
        ab1 = pa.ability1
        ab2 = pa.ability2
        hab = pa.hide_ability
        if ab1 != '' and ab1 in pokemon_ability:
            pokemon_ability[ab1] = pokemon_ability[ab1] + 1
        elif ab1 != '' and ab1 not in pokemon_ability:
            pokemon_ability[ab1] = 1
        if ab2 != '' and ab2 in pokemon_ability:
            pokemon_ability[ab2] = pokemon_ability[ab2] + 1
        elif ab2 != '' and ab2 not in pokemon_ability:
            pokemon_ability[ab2] = 1
        if hab != '' and hab in pokemon_ability:
            pokemon_ability[hab] = pokemon_ability[hab] + 1
        elif hab != '' and hab not in pokemon_ability:
            pokemon_ability[hab] = 1
    pokemon_ability = sorted(pokemon_ability.items(),
                             key=lambda x: x[1], reverse=True)
    return pokemon_ability
