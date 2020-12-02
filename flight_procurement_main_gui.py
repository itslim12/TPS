# procurement_main_gui.py
# France Cheong
# 22/11/2018

# ########
# Packages
# ########

import tkinter as tk
import os

# #################################################
# Import any of your classes defined in other files
# #################################################
"""
#Import database.py to get a session to a particular db
#from staff_gui import StaffGUI # To communicate with staff GUI
#from flight_gui import FlightGUI # To communicate with Flight GUI
"""

from staff_gui import StaffGUI
from flight_gui import FlightGUI

"""
    GUI class to perform CRUD operations on the main page of the Procurement system.
"""  
class ProcurementGUI():
    """
    #This is used as an initialiser to be used to "instantiate" attributes of the class.
    #Create a high level frame which contains the entire GUI 

    """
    def __init__(self,root):   
        # Reference to current GUI stored as an object attribute
        self.current_gui = None
        
        # 900x500 pixels in the middle of the screen
        #Can minimise to 0x0 pixels

        #Reference to root window stored as an object attribute
        self.root = tk.Tk()
        root.withdraw()

        self.root.title("Airline Procurement System")
        self.root.geometry('900x600')

        menubar = tk.Menu(self.root)

        # Employee menu
        # Create a menu item
        # Menu items not in a pulldown do not appear on the Mac!
        # Need to add the menu item in a pulldown menu
        #menubar.add_command(label="Employee", command=self.create_employee_gui) 

        # Create Employee pulldown menu
        staff_menu = tk.Menu(menubar, tearoff=0)
        staff_menu.add_command(label="Staff", command=self.create_staff_gui) 
        # Add Employee pulldown menu to toplevel menu bar
        menubar.add_cascade(label="Staff", menu=staff_menu)

        #Product menu (pulldown)
        # Create a pulldown menu
        flight_menu = tk.Menu(menubar, tearoff=0)
        # Add menu items
        flight_menu.add_command(label="Flight",
            command=self.create_flight_gui)
        # Add pulldown menu to toplevel menu
        menubar.add_cascade(label="Flight", menu=flight_menu)
        # Exit menu item 
        # Does not work on the Mac, replace with a pull down
        # menubar.add_command(label="Quit", command=self.exit)
        
        # Create Customer pulldown menu
        customer_menu = tk.Menu(menubar, tearoff=0)
        customer_menu.add_command(label="Customer", command=self.create_customer_gui) 
        # Add Employee pulldown menu to toplevel menu bar
        menubar.add_cascade(label="Customer", menu=customer_menu)
        # Display the toplevel menu
        self.root.config(menu=menubar)

        # Create itinenary pulldown menu
        itinenary_menu = tk.Menu(menubar, tearoff=0)
        itinenary_menu.add_command(label="Itinenary", command=self.create_itinenary_gui) 
        # Add Employee pulldown menu to toplevel menu bar
        menubar.add_cascade(label="Itinenary", menu=itinenary_menu)
        # Display the toplevel menu
        self.root.config(menu=menubar)

         # Create Exit pulldown menu
        exit_menu = tk.Menu(menubar, tearoff=0)
        exit_menu.add_command(label="Exit", command=self.exit) 
        # Add Exit pulldown menu to toplevel menu bar
        menubar.add_cascade(label="Exit", menu=exit_menu)
            
    # Functions to create child frames 
    # when menu options are selected
    """
    Opens up the staff GUI
    """
    def create_staff_gui(self):
        os.system('python staff_gui.py')
    """
    exits the program
    """
    def exit(self):
        exit()
    """
    Opens up the flight GUI
    """
    def create_flight_gui(self):
        os.system('python flight_gui.py')

        pass


    def create_customer_gui(self):
        pass 

    def create_itinenary_gui(self):
        pass   

    def create_product_report_gui(self):
        pass        

    def create_category_report_gui(self):
        pass

    

# ###########
# Main method
# ###########

if __name__ == '__main__':
    root = tk.Tk()
    ProcurementGUI(root)
    root.mainloop()
            