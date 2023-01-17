import pandas as pd
from sqlalchemy import create_engine, Integer, Column, VARCHAR, UniqueConstraint
from sqlalchemy.orm import declarative_base, Session


def connect(user, password, db, host='localhost', port=5432):
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)
    return create_engine(url, echo=True, future=True, pool_size=5, pool_recycle=3600)


engine = connect('test', '123456', 'pokemon')
Base = declarative_base()


class Pokemon(Base):
    __tablename__ = "pokemon_info"
    __table_args__ = (UniqueConstraint("english_name", "japanese_name"),)
    id = Column(Integer, primary_key=True)
    english_name = Column(VARCHAR(100), unique=True)
    japanese_name = Column(VARCHAR(100), unique=True)
    type1 = Column(VARCHAR(100))
    type2 = Column(VARCHAR(100))
    official_rom = Column(VARCHAR(100))


Base.metadata.create_all(engine)

session = Session(engine)
objects = []
df = pd.read_csv("data/pokemon.csv")
for data in df.itertuples():
    obj = Pokemon(id=data.id, english_name=data.english_name, type1=data.type1, type2=data.type2,
                  japanese_name=data.japanese_name, official_rom=data.official_rom)
    objects.append(obj)
session.bulk_save_objects(objects)
session.commit()
