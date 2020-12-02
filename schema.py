# schema.py
# France Cheong
# 21/01/2019

# Import packages
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, Float, Date, ForeignKey
# Used by classes PurchaseOrder and PurchaseOrderItem
from sqlalchemy.orm import relationship 
"""
# Get a base class from which all mapped classes should inherit
"""
Base = declarative_base()
"""
This class is a variable schema for the class Staff
"""
# Staff class should inherit from Base class
# Note that "Staff" is spelt with an UPPERCASE "S"
class Staff(Base): 

    # Define the name of the table i.e. staff (all lower case, singular)
    # Note that "staff" is spelt with a LOWERCASE "s"
    # Also note that there are TWO UNDERSCORES before and after "tablename"
    __tablename__ = 'staff'

    # Define the column names, types, primary key, foreign keys, 
    # null values allowed, unique, etc
    # Column names should be all lower case, use an underscore to concatenate
    staff_id = Column(Integer, primary_key=True) # primary key
    first_name = Column(String(255), nullable=False) # non null
    last_name = Column(String(255), nullable=False) # non null
    title = Column(String(255), nullable=False) # non null, unique
    sex = Column(String(255),nullable=False ) # non null, unique
    email = Column(String(255), nullable=False, unique=True) # non null, unique
    contact_no = Column(String(20), nullable=False, unique=True) # non null, unique
    pass

"""
This class is a variable schema for the class Customer
"""
class Customer(Base):

    # Define the name of the table i.e. supplier (all lower case, singular)
    __tablename__ = 'customer'

    # Define the column names, types, primary key, foreign keys, 
    # null values allowed, unique, etc
    # Column names should be all lower case, use an underscore to concatenate
    customer_id = Column(Integer, primary_key=True) # primary key
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    street_address = Column(String(255), nullable=False)
    suburb = Column(String(255), nullable=False)
    postcode = Column(String(255), nullable=False)
    state = Column(String(255), nullable=False)
    country = Column(String(255), nullable=False)
    contact_no = Column(String(20), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    
"""
This class is a variable schema for the class Customer
"""   
class Flight(Base):

    # Define the name of the table 
    __tablename__ = 'flight' # i.e. product (all lower case, singular)

    # Define the column names, types, primary key, foreign keys, 
    # null values allowed, unique, etc
    # Column names should be all lower case, use an underscore to concatenate
    flight_id = Column(Integer, primary_key=True) # primary key
    airline_name = Column(String(255), nullable=False)
    from_location = Column(String(255), nullable=False)
    to_location = Column(String(255), nullable=False)
    depature_time = Column(Integer, nullable=False)
    arrival_time = Column(Integer, nullable=False)
    duration = Column(Integer, nullable=False) 
    total_seats = Column(Integer, nullable=False)
    flight_price = Column(Integer, nullable=False)

"""
This class is a variable schema for the class Itinerary
"""    
# PurchaseOrder class should inherit from Base class     
class Itinerary(Base):

    # Define the name of the table
    __tablename__ = 'itinerary' # i.e. purchase_order (all lower case, singular)

    # Define the column names, types, primary key, foreign keys, null values allowed, unique, etc
    # Column names should be all lower case, use an underscore to concatenate
    booking_id = Column(Integer, primary_key=True) # primary key
    customer_id = Column(Integer, ForeignKey("customer.customer_id")) # foreign key
    staff_id = Column(Integer, ForeignKey("staff.staff_id")) # foreign key
    order_date = Column(Date, nullable=False)
    flight_id = Column(String(255), ForeignKey("flight.flight_id")) # foreign key
    flight_date = Column(Date, nullable= False)
    quantity = Column(Integer, nullable=False)
    total_price = Column(Integer, nullable=False)
    transaction_status = Column(String(255), nullable=False)