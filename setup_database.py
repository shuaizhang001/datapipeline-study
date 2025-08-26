import sqlalchemy as sa
import os
from sqlalchemy import Column, Float
DATABASE_URL = "sqlite:///data/buoy_data.db"

def setup_database():
    """create database and tables"""
    os.makedirs('data',exist_ok=True)
    engine = sa.create_engine(DATABASE_URL)
    metadata = sa.MetaData()

    #Define table structure
    buoy_data = sa.Table('buoy_readings',
                         metadata,
                         Column('id', sa.Integer,primary_key=True,autoincrement=True),
                         Column('station_id', sa.String(20)),
                         Column('timestamp',sa.DateTime,unique=True),
                         Column('temperature', Float),
                         Column('sigma',Float),
                         Column('data_quality',sa.String(10)),
                         Column('created_at',sa.DateTime,default=sa.func.now())
                         )

    #Create tables
    metadata.create_all(engine)
    print(f"Database setup complete:{DATABASE_URL}")
    return engine

if __name__ == "__main__": # so it only runs when running a script, doesn't run when it's been called as a lib or imported
    setup_database()


