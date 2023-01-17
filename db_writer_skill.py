import pandas as pd
from sqlalchemy import create_engine, Integer, Column, VARCHAR, UniqueConstraint
from sqlalchemy.orm import declarative_base, Session


def connect(user, password, db, host='localhost', port=5432):
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)
    return create_engine(url, echo=True, future=True, pool_size=5, pool_recycle=3600)


engine = connect('test', '123456', 'pokemon')
Base = declarative_base()


class Skill(Base):
    __tablename__ = "skill"
    __table_args__ = (UniqueConstraint("name"),)
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(100), unique=True)
    type = Column(VARCHAR(100))
    category = Column(VARCHAR(100))
    pp = Column(VARCHAR(100))
    power = Column(VARCHAR(100))
    accuracy = Column(Integer)
    gen = Column(VARCHAR(10))


Base.metadata.create_all(engine)
session = Session(engine)
objects = []
df = pd.read_csv("data/skill.csv")
for data in df.itertuples():
    data_id, data_name, data_type, data_category, data_pp, data_power, data_accuracy, data_gen = \
        data.id, data.name, data.type, data.category, data.pp, data.power, data.accuracy, data.gen
    data_pp = data_pp.replace("*", "")
    data_power = data_power.replace("*", "")
    data_power = None if '—' in data_power else data_power
    data_accuracy = data_accuracy.replace("*", "").replace("%", "")
    data_accuracy = None if '—' in data_accuracy else data_accuracy
    obj = Skill(id=data_id, name=data_name, type=data_type, category=data_category,
                pp=data_pp, power=data_power, accuracy=data_accuracy, gen=data_gen)
    objects.append(obj)
session.bulk_save_objects(objects)
session.commit()
