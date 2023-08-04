import os
import pandas as pd
from flask import *
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
datapath = "./data"


class PokemonInfo(db.Model):
    __tablename__ = "pokemon_info"
    idx = db.Column(db.Integer, autoincrement=True, primary_key=True)
    id = db.Column(db.Integer)
    href = db.Column(db.String(100))
    name = db.Column(db.String(100))
    detail = db.Column(db.String(100))
    type1 = db.Column(db.String(100))
    type2 = db.Column(db.String(100))
    gen = db.Column(db.String(10))


class Skill(db.Model):
    __tablename__ = "skill"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    type = db.Column(db.String(100))
    category = db.Column(db.String(100))
    pp = db.Column(db.String(100))
    power = db.Column(db.String(100))
    accuracy = db.Column(db.Integer)
    gen = db.Column(db.String(10))


class Ability(db.Model):
    __tablename__ = "ability"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    gen = db.Column(db.String(10))


class PokemonAbility(db.Model):
    __tablename__ = "pokemon_ability"
    idx = db.Column(db.Integer, autoincrement=True, primary_key=True)
    id = db.Column(db.Integer)
    name = db.Column(db.String(100))
    detail = db.Column(db.String(100))
    ability1 = db.Column(db.String(100))
    ability2 = db.Column(db.String(100))
    hide_ability = db.Column(db.String(100))


def save_pokemon_info():
    session = db.session
    objects = []
    df = pd.read_csv(os.path.join(datapath, "pokemon.csv"))
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
    session = db.session
    objects = []
    df = pd.read_csv(os.path.join(datapath, "skill.csv"))
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
    session = db.session
    objects = []
    df = pd.read_csv(os.path.join(datapath, "ability.csv"))
    for data in df.itertuples():
        obj = Ability(id=data.id, name=data.name,
                      description=data.description,
                      gen=data.gen)
        objects.append(obj)
    session.bulk_save_objects(objects)
    session.commit()


def save_pokemon_ability():
    session = db.session
    objects = []
    df = pd.read_csv(os.path.join(datapath, "pokemon_ability.csv"))
    for data in df.itertuples():
        ability1 = data.ability1
        ability2 = data.ability2
        hide_ability = data.hide_ability
        ability1 = ability1.replace("*", "") if type(ability1) == str else ''
        ability2 = ability2.replace("*", "") if type(ability2) == str else ''
        hide_ability = hide_ability.replace(
            "*", "") if type(hide_ability) == str else ''
        obj = PokemonAbility(id=data.id, name=data.name, detail=data.detail,
                             ability1=ability1, ability2=ability2,
                             hide_ability=hide_ability)
        objects.append(obj)
    session.bulk_save_objects(objects)
    session.commit()


with app.app_context():
    db.drop_all()
    db.create_all()
    save_pokemon_info()
    save_skill()
    save_ability()
    save_pokemon_ability()
