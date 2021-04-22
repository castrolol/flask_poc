import os

def database_uri():
    return "mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4".format(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_DATABASE"),
    )