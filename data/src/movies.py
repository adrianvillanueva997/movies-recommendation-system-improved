import os
import pandas as pd
from sqlalchemy import create_engine, Column, String, exc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text
from dotenv import load_dotenv

load_dotenv()
engine = create_engine(os.getenv("db_data"))
df = pd.read_csv("data/movies.csv")
print(str(df["genres"][0]).split("|"))
with engine.connect() as conn:
    print("[INFO] Inserting movies.")
    query = text('INSERT INTO public."Movie" (title)VALUES(:_movie);')
    for i in range(0, len(df["title"])):
        try:
            movie = (df["title"][i])
            print(f"Inserting: {movie}")
            insert = conn.execute(query, _movie=movie)
        except Exception as e:
            print(e)
    try:
        query = text(
            'INSERT INTO public."Genres"("Genre", "movieId")VALUES(:_genre, :_id);')
        _id = 1
        for i in range(0, len(df["genres"])):
            genres = str(df["genres"][i]).split("|")
            print(f"Inserting: {genres}")
            for genre in genres:
                conn.execute(query, _id=_id, _genre=genre)
            _id += 1
    except Exception as e:
        print(e)
