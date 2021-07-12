import os
import pandas as pd
from sqlalchemy import create_engine, Column, String, exc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text
from dotenv import load_dotenv


class Movie:
    title = Column(String, nullable=False)

    def __init__(self, title) -> None:
        self.title = title

    def __repr__(self) -> str:
        return f'Movie({self.title})'

    def __str__(self) -> str:
        return self.title


load_dotenv()
engine = create_engine(os.getenv("db_data"))
df = pd.read_csv("data/movies.csv")
print(str(df["genres"][0]).split("|"))
with engine.connect() as conn:
    query = text('INSERT INTO public."Movies"(title)VALUES(:_movie);')
    print("[INFO] Inserting movies.")
    try:
        for i in range(0, len(df["title"])):
            movie = (df["title"][i])
            insert = conn.execute(query, _movie=movie)
        print("test")
    except Exception as e:
        print(e)
    print("[INFO] Inserting tags")
