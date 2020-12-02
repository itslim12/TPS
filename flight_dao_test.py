# product_dao_test.py
# France Cheong
# 21/01/2019

# Import packages
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

"""
# Import Dao
 """
from flight_dao import FlightDAO

# Database location
# Uniform Resource Identifier (URI) generic version of URL
# URI - a string of characters that unambiguously identifies a particular resource
DATABASE_URI = 'sqlite:///app.db'
# File app.db will be created in the folder where the python script is found

"""
# Create Database method to allow the other functions to run
"""
def get_db_session():
    engine = create_engine(DATABASE_URI, echo=False)
    # echo=False means do not show generated SQL statements
    # Can be set to echo=True to show SQL
    Session = sessionmaker(bind=engine)
    session = Session()
    return session 
"""
# test create function for flight_dao is functionable
"""
def test_create():
    # Get a session
    session = get_db_session()
    
    # Instantiate the Product DAO
    prod = FlightDAO()

    # Setup the data as a dictionary
    data = {}
    #data['flight_id'] = "3" # No
    data['airline_name'] = "Bob Airlines"
    data['from_location'] = "Tullamarine Aiport, Melbourne"
    data['to_location'] = "Changi Airport, Singapore"
    data['depature_time'] = 1020
    data['arrival_time'] = 1420
    data['duration'] = 230
    data['total_seats'] = 350
    data['flight_price'] = 3500
    

    # Call the create() method from the DAO
    # and pass the dictionary as parameter
    result = prod.create(session, data)

    # Print the result
    print(result)

    # Close the session
    session.close()
"""
# test find_by_id function for flight_dao 
"""
def test_find_by_id():
    # Get a session
    session = get_db_session()
    
    # Instantiate the Product DAO
    prod = FlightDAO()

    # Assign an product_id
    flight_id = 1 # exists
    #pproduct_id = 5 # does not exist?
    
    # Call the find_by_id() method from the DAO
    # and pass the product_id as parameter - could pass it directly
    result = prod.find_by_id(session, flight_id)

    # Print the result
    print(result)

    # Close the session
    session.close()
"""
# test find_find_all function for flight_dao 
"""
def test_find_all():
    # Get a session
    session = get_db_session()
    
    # Instantiate the Product DAO
    prod = FlightDAO()

    # Call the find_all() method from the DAO
    result = prod.find_all(session)

    # Print the result
    print(result)

    # Close the session
    session.close()    
"""
# test find_find_ids function for flight_dao
"""
def test_find_ids():
    # Get a session
    session = get_db_session()
    
    # Instantiate the Product DAO
    prod = FlightDAO()

    # Call the find_ids() method from the DAO
    result = prod.find_ids(session)

    # Print the result
    print(result)

    # Close the session
    session.close()    
"""
# test update function for flight_dao 
"""
def test_update():
    # Get a session
    session = get_db_session()

    # Instantiate the Product DAO
    prod = FlightDAO()

    # Assign an product_id 
    flight_id = 1 # exists
    #product_id = 5 # does not exist?

    # Create a dictionary and add items
    # Do not add the employee_id to the dict
    data = {}
    #data['flight_id'] = "3"  # No
    data['airline_name'] = "Bob Airlines"
    data['from_location'] = "Tullamarine Aiport, Melbourne"
    data['to_location'] = "Changi Airport, Singapore"
    data['depature_time'] = 1020
    data['arrival_time'] = 1420
    data['duration'] = 230
    data['total_seats'] = 450 
    data['flight_price'] = 4244

    # Call the update() method from thet DAO
    # and pass the product_id and data as parameters    
    result = prod.update(session, flight_id, data)

    # Print the result
    print(result)

    # Close the session
    session.close()    
"""
# test delete function for flight_dao 
"""
def test_delete():
    # Get a session
    session = get_db_session()
        
    # Instantiate the Product DAO
    prod = FlightDAO()

    # Assign an product_id
    flight_id = 1 # exists
    #product_id = 5 # does not exist?

    # Call the delete() method from the DAO
    # and pass the pproduct_id as parameter - could pass it directly
    result = prod.delete(session, flight_id)

    # Print the result
    print(result)

    # Close the session
    session.close()          

"""
Run this line when the name of this file is called
"""
if __name__ == "__main__":

    print("\nTesting ...")

    test_create()
    
    test_find_by_id()

    test_find_all()

    test_find_ids()

    test_update()

    test_delete()

