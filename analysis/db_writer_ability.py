import pandas as pd
from sqlalchemy import create_engine, Integer, Column, VARCHAR, UniqueConstraint
from sqlalchemy.orm import declarative_base, Session


def connect(user, password, db, host='localhost', port=5432):
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)
    return create_engine(url, echo=True, future=True, pool_size=5, pool_recycle=3600)


engine = connect('test', '123456', 'pokemon')
Base = declarative_base()


class Ability(Base):
    __tablename__ = "ability"
    __table_args__ = (UniqueConstraint("name"),)
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(100), unique=True)
    description = Column(VARCHAR(1000))
    gen = Column(VARCHAR(10))


Base.metadata.create_all(engine)

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
