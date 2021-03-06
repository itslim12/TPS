# product_dao.py
# France Cheong
# 11/12/2018

# Import packages
# From file xxx.py import class Xxxx
# Note: Filenames with hyphens cannot be imported, use underscores
from schema import Flight
"""
    #DAO class to perform basic operations on the employee table in the database.
"""
class FlightDAO():
    """
This function creates flights by inserting data to linked variables 

    """
    def create(self, session, data):

        # Print info for debugging
        print("\nCreating a flight ...") #\n means print("\n") a blank line
        print(data)

        # Instantiate an object of the mapped Product class - defined in schema.py
        # SKip the product_id when inserting as it will be generated by the database
        flight = Flight(airline_name=data['airline_name'],  # skip the product_id
                    from_location=data['from_location'], 
                    to_location=data['to_location'], 
                    depature_time=data['depature_time'],
                    arrival_time=data['arrival_time'],
                    duration=data['duration'],
                    total_seats=data['total_seats'],
                    flight_price=data['flight_price']
                    )
        # Get the session to add the employee object            
        session.add(flight)
        session.commit() # Must commit to save the record permanently

        # Create a blank dictionary to return the result
        result = {}  
        result['message'] = 'Flight added successfully!'
        inserted_flight_id = flight.flight_id
        result['flight_id'] = inserted_flight_id

        return result # return the result as a dictionary 
    """
    This function find flight by searching for the requested flight_id 
    """    
    def find_by_id(self, session, flight_id):

        # Print info for debugging
        print("\nFinding a flight ...")
        print(flight_id)
       

        # Get the session to query the Product class
        # And get by the primary key i.e. product_id
        prod = session.query(Flight).get(flight_id)
        
        # Create a blank dictionary to return the result
        result = {}

        # prod is a single Alchemy object - no need for a loop to process
        if not prod:
            # If no flight found i.e. prod is none
            result['message'] = "Flight NOT found"
        else:
            # Else grab the values in the returned SQLalchemy object
            # And build another python dictionary
            d = {} # Create an empty dict and add items to it
            d['flight_id'] = prod.flight_id # include the product_id
            d['airline_name'] = prod.airline_name
            d['from_location'] = prod.from_location
            d['to_location'] = prod.to_location
            d['depature_time'] = prod.depature_time
            d['arrival_time'] = prod.arrival_time
            d['duration'] = prod.duration
            d['total_seats'] = prod.total_seats
            d['flight_price'] = prod.flight_price


            # Store the prod dict in the result dict under key "flight"
            result['flight'] = d
            #session.commit() # not needed for find as not saving changes            
        
        # Note that the return is not part of the if/else block
        # Ensure it's indented to the left
        return result # return the result as a dictionary
    """
    This function finds all flight available in the database
    """
    def find_all(self, session):

        # Print info for debugging
        print("Finding all flights ...")

        # Create a blank dictionary to return the result
        result = {}

        # Get the session to query the Product class and get all (may wish to sort)
        rows = session.query(Flight).all()

        if not rows:
            result['message'] = "No flights found!"
        else:
            # Convert list of Alchemy objects to a list of dictionaries
            list_prod = [] # Create an empty list to append prod dicts
            for x in rows: # rows is a list of Alchemy objects - process one by one
                d = {} # Create an empty dict and add items to it
                d['flight_id'] = x.flight_id
                d['airline_name'] = x.airline_name
                d['from_location'] = x.from_location
                d['to_location'] = x.to_location
                d['depature_time'] = x.depature_time
                d['arrival_time'] = x.arrival_time
                d['duration'] = x.duration
                d['total_seats'] = x.total_seats
                d['flight_price'] = x.flight_price

                list_prod.append(d) # Append the employee dict to the employee list
                pass    

            # Store the prod list in the result dict under key "flights"               
            result['flights'] = list_prod

        # return the result as a dictionary
        return result 
    """
    This function shows all the flight ids available in the database 
    """
    
    def find_ids(self, session):
        """
        This is a special method similar to find_all but returns product_ids only, 
        not the full details
        """

        # Print info for debugging
        print("\nFinding all flight ids ...")

        # Create a blank dictionary to return the result
        result = {}

        # Get the list of flights from the database
        rows = session.query(Flight).all()

        if not rows:
            result['message'] = "No flight found!"
        else:
            # Convert list of Alchemy objects to a list of dictionaries
            list_ids = []
            for x in rows:
                list_ids.append(x.flight_id)
                pass               

            # Store the list of ids in the result dict under key "employee_ids"
            result['flight_ids'] = list_ids

        return result # return the result as a dictionary
    """
    This function updates selected flights in the database
    """
    def update(self, session, flight_id, data):

        # Print info for debugging
        print("Updating flight ...")
        print(flight_id)
        print(data)

        result = {}

        # Find the flight record  
        prod = session.query(Flight).get(flight_id)

        # What happens if the flight is not found?
        if prod:
            #prod.product_id = data['product_id'] # Not the primary key!
            prod.airline_name = data['airline_name']
            prod.from_location = data['from_location']
            prod.to_location = data['to_location']
            prod.depature_time = data['depature_time']
            prod.arrival_time = data['arrival_time']
            prod.duration = data['duration']
            prod.total_seats = data['total_seats']
            prod.flight_price = data['flight_price']


            session.commit() 

            # Store an appropriate message in the result dict under key "message"
            result['message'] = "Flight updated!"     
        else:
            result['message'] = "Flight not found!"

        return result # return the result as a dictionary
    """
    This function deletes selected flights in the database
    """
    def delete(self, session, flight_id):

        # Print info for debugging
        print("\nDeleting Flight ...")
        print(flight_id)
 
        # Create a blank dictionary to return the result
        result = {}

        # Find the record and get the session to delete it  
        prod = session.query(Flight).get(flight_id)
        # What happens if the flight is not found?         
        if prod:
            session.delete(prod)          
            session.commit()    

            # Store an appropriate message in the result dict under key "message"
            result['message'] = "Flight deleted"  
        else:  
            result['message'] = "Flight not found"

        return result # return the result as a dictionary        