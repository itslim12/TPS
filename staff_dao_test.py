# product_dao_test_stubs.py
# France Cheong
# 21/01/2019

# Import packages
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

"""
# Import Dao
 """
from staff_dao import StaffDAO

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
# test create function for staff_dao is functionable
"""
def test_create():
    # Get a session
    session = get_db_session()
    
    # Instantiate the Staff DAO
    emp = StaffDAO()

    # Alternatively, the data could be set up in JSON format
    data = {
        'first_name':"Bob",
        'last_name': "Mare",
        'title': "Mr",
        'sex':'Male',
        'email': "b.mare12@gmail.com",
        'contact_no': "(02) 9999 6466" # no comma on last item
    }

    # Call the create() method from the DAO
    # and pass the dictionary as parameter
    result = emp.create(session, data)

    # Print the result
    print(result)

    # Close the session
    session.close()

"""
# test find_by_id function for staff_dao 
"""
def test_find_by_id():
     # Get a session
    session = get_db_session()
    
    # Instantiate the Staff DAO
    emp = StaffDAO()

    # Assign an staff_id
    staff_id = 1 # exists
    #staff_id = 2 # does not exist?
    
    # Call the find_by_id() method from the DAO
    # and pass the staff_id as parameter - could pass it directly
    result = emp.find_by_id(session, staff_id)

    # Print the result
    print(result)
    
    # Close the session
    session.close()
"""
# test find_find_all function for staff_dao 
"""
def test_find_all():
        # Get a session
    session = get_db_session()
    
    # Instantiate the Staff DAO
    emp = StaffDAO()

    # Call the find_all() method from the DAO
    result = emp.find_all(session)

    # Print the result
    print(result)

    # Close the session
    session.close()       
"""
# test find_find_ids function for staff_dao
"""
def test_find_ids():
       # Get a session
    session = get_db_session()
    
    # Instantiate the Staff DAO
    emp = StaffDAO()

    # Call the find_ids() method from the DAO
    result = emp.find_ids(session)

    # Print the result
    print(result)

    # Close the session
    session.close()    

"""
# test update function for staff_dao 
"""

def test_update():
    # Get a session
    session = get_db_session()

    # Instantiate the Staff DAO
    emp = StaffDAO()

    # Assign an staff_id 
    staff_id = 1 # exists
    #staff_id = 2 # does not exist?

    # Create a dictionary and add items
    # Do not add the staff_id to the dict
    data = {}
    data['first_name'] = "Joe"
    data['last_name'] = "Marly"
    data['title'] = "Mr"
    data['sex'] = 'Male'
    data['email'] = "j.cheong@gmail.com"
    data['contact_no'] = "(02) 8888 9999"
    # Alternatively, the data could be defined in JSON format
        
    # Call the update() method from the DAO
    # and pass the staff_id and data as parameters    
    result = emp.update(session, staff_id, data)

    # Print the result
    print(result)

    # Close the session
    session.close()    

"""
# test delete function for staff_dao 
"""
def test_delete():
     # Get a session
    session = get_db_session()
        
    emp = StaffDAO()

    # Assign an staff_id
    staff_id = 1 # exists
    #staff_id = 2 # does not exist?

    # Call the delete() method from the DAO
    # and pass the staff_id as parameter - could pass it directly
    result = emp.delete(session, staff_id)

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

