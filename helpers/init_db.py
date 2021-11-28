from db.orm import start_mappers, create_tables

def init():
    start_mappers()
    create_tables()
