# create_tables.py
# France Cheong
# 21/01/2019

# Import packages
from sqlalchemy import create_engine

from schema import Base 
"""
# Database location
"""
DATABASE_URI = 'sqlite:///app.db'

engine = create_engine(DATABASE_URI, echo=False)

"""
# Create the database and the tables
"""
Base.metadata.create_all(engine)
print("Procurement database created ...")
print("Use DB Browser for SQLite to view the contents of the database app.db ...")