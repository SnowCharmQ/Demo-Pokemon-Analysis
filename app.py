from flask import *

import utils

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/time')
def get_time():
    return utils.get_time()


@app.route('/num')
def get_num():
    pokemon = utils.get_pokemon_num()
    skill = utils.get_skill_num()
    ability = utils.get_ability_num()
    return jsonify({"pokemon": pokemon, "skill": skill, "ability": ability, "gen": 9})


if __name__ == '__main__':
    app.run()
