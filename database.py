# database.py
# France Cheong
# 29/01/2019

# ########
# Packages
# ########
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URI = 'sqlite:///app.db'

def get_db_session():
    engine = create_engine(DATABASE_URI, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session 