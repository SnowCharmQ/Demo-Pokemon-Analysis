from flask import *
from flask_sqlalchemy import SQLAlchemy

import utils

from config import app


@app.errorhandler(404)
def not_found(e):
    return render_template('index.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/time')
def get_time():
    return {"time": utils.get_time()}


@app.route('/num')
def get_num():
    pokemon = utils.get_pokemon_num()
    skill = utils.get_skill_num()
    ability = utils.get_ability_num()
    return jsonify({"pokemon": pokemon, "skill": skill, "ability": ability, "gen": 9})


@app.route('/gen')
def get_gen_curve():
    gens = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    pokemons, skills, abilities = [], [], []
    pokemon_dict = utils.get_pokemon_gen()
    skill_dict = utils.get_skill_gen()
    ability_dict = utils.get_ability_gen()
    for gen in gens:
        pokemon = pokemon_dict.get(gen)
        pokemons.append(pokemon if pokemon else 0)
        skill = skill_dict.get(gen)
        skills.append(skill if skill else 0)
        ability = ability_dict.get(gen)
        abilities.append(ability if ability else 0)
    return jsonify({"gen": gens, "pokemon": pokemons, "skill": skills, "ability": abilities})


@app.route('/type')
def get_pokemon_type():
    return jsonify(utils.get_pokemon_type())


@app.route('/ability')
def get_pokemon_ability():
    pokemon_ability = utils.get_pokemon_ability()
    pokemon_ability = [list(x) for x in pokemon_ability]
    pokemon_ability = pokemon_ability[:10]
    pokemon_ability.reverse()
    return pokemon_ability


@app.route('/detail', methods=['post'])
def get_pokemon_detail():
    data = request.get_json()
    msg = data.get('msg')
    detail = utils.query_pokemon(msg)
    if detail is not None:
        detail['code'] = 200
        detail.pop('_sa_instance_state')
        return jsonify(detail)
    else:
        return jsonify({"code": 404})
