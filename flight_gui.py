# product_gui.py
# France Cheong
# 11/12/2018

# ########
# Packages
# ########
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk # for combobox


"""
#Import database.py to get a session to a particular db
#from flight_dao import FlightDAO # To communicate with Product table
#from validation import Validation # To validate the entries made on the form
"""
import database as db
from flight_dao import FlightDAO
from validation import Validation

"""
    GUI class to perform CRUD operations on the flight table in the database.
"""  
class FlightGUI():
    """
    This is used as an initialiser to be used to "instantiate" attributes of the class.
    """
    def __init__(self):
    
        self.flt_dao = FlightDAO()

        self.validator = Validation()


        self.flight_id = tk.IntVar()
        self.airline_name = tk.StringVar()
        self.from_location = tk.StringVar()
        self.to_location = tk.StringVar()
        self.depature_time = tk.IntVar()
        self.arrival_time = tk.IntVar()
        self.duration = tk.IntVar()
        self.total_seats = tk.IntVar()
        self.flight_price = tk.IntVar()


        # List of employee ids - lb for listbox
        self.lb_ids = None
        
        # Messagebox title
        self.mb_title_bar = "Employee CRUD"

        pass 
        
    """
    Create a high level frame which contains the entire GUI 
    """
    def create_gui(self, root):
        print("Creating employee GUI ...")

        prod_frame = tk.Frame(root)
        prod_frame.pack()

        form_frame = tk.Frame(prod_frame)
        form_frame.pack()

        #Widgets

        #Row 0 :title
        tk.Label(form_frame, font=('arial', 10),
                    text = "Flights").grid(row=0, column=0, columnspan=3) 

        #row 1 :product_id label, product_id entry and list_of ids label
        tk.Label(form_frame, text= "Flight Id", font=('arial', 10),
                width=20, anchor="e", bd=1,
                pady=10, padx=10).grid(row=1, column=0)
        tk.Entry(form_frame, textvariable=self.flight_id, width=30, bd=1, 
                 state=tk.DISABLED).grid(row=1, column=1)
        tk.Label(form_frame, text= "Flight IDs",
                 font=('arial', 10)).grid(row=1, column=2) 

        self.lb_ids = tk.Listbox(form_frame)
        self.lb_ids.grid(row=1, column=2, rowspan=6)
        # Set the method to be called when an item is clicked on the listbox
        self.lb_ids.bind('<<ListboxSelect>>', self.on_list_select)
        
        #row 2 : product name label, product name entry
        tk.Label(form_frame, text= "Airline Name", font=('arial', 10),
                width=20, anchor="e", bd=1,
                pady=10, padx=10).grid(row=2, column=0)
        VALUES = ("Bob Airlines","Malaysia Airlines","Qantas Airlines")
        combo_prod_cat = ttk.Combobox(form_frame, state="normal",textvariable=self.airline_name,
                    values=VALUES, width=20)
        combo_prod_cat.grid(row=2, column=1, sticky="w")
        

        #row 3 - Depature label, depature desc entry
        tk.Label(form_frame, text= "Depature", font=('arial', 10),
                width=20, anchor="e", bd=1,
                pady=10, padx=10).grid(row=3, column=0)
        VALUES = ("Tullamarine Airpot, Melbourne","Changi Airport, Singapore", "Sydney Airport,Sydney")
        combo_prod_cat = ttk.Combobox(form_frame, state="normal",textvariable=self.from_location,
                    values=VALUES, width=20)
        combo_prod_cat.grid(row=3, column=1, sticky="w") 
        
        #row 4 - Arrival label , arrival desc entry
        tk.Label(form_frame, text= "Arrival", font=('arial', 10),
                width=20, anchor="e", bd=1,
                pady=10, padx=10).grid(row=4, column=0)
        VALUES = ("Tullamarine Airpot, Melbourne","Changi Airport, Singapore", "Sydney Airport,Sydney")
        combo_prod_cat = ttk.Combobox(form_frame, state="normal",textvariable=self.to_location,
                    values=VALUES, width=20)
        combo_prod_cat.grid(row=4, column=1, sticky="w")

        #row 5 - Depature time label, Depature time combobox
        tk.Label(form_frame, text= "Depature Time", font=('arial', 10),
                width=20, anchor="e", bd=1,
                pady=10, padx=10).grid(row=5, column=0)
        VALUES = (1530,2230,1430,1120)
        combo_prod_cat = ttk.Combobox(form_frame, state="normal", textvariable=self.depature_time,
                    values=VALUES, width=10)
        combo_prod_cat.grid(row=5, column=1, sticky="w")

        #row 6 - Arrival time label, depature time combobox
        tk.Label(form_frame, text= "Arrival Time", font=('arial', 10),
                width=20, anchor="e", bd=1,
                pady=10, padx=10).grid(row=6, column=0)
        VALUES = (1530,2230,1430,1120)
        combo_prod_cat = ttk.Combobox(form_frame, state="normal", textvariable=self.arrival_time,
                    values=VALUES, width=10)
        combo_prod_cat.grid(row=6, column=1, sticky="w")

        #row 7 - Duration label, duration time combobox
        tk.Label(form_frame, text= "Duration", font=('arial', 10),
                    width=20, anchor="e", bd=1,
                    pady=10, padx=10).grid(row=7, column=0)
        self.txt_prod_desc = tk.Entry(form_frame,textvariable=self.duration,width=30, bd=1)
        self.txt_prod_desc.grid(row=7, column=1)

        #row 8 - total seats label, total seats entry
        tk.Label(form_frame, text= "Total Seats", font=('arial', 10),
                    width=20, anchor="e", bd=1,
                    pady=10, padx=10).grid(row=8, column=0)
        self.txt_prod_desc = tk.Entry(form_frame, textvariable=self.total_seats,width=30, bd=1)
        self.txt_prod_desc.grid(row=8, column=1)
        
        #row 8 - total seats label, total seats entry
        tk.Label(form_frame, text= "Price", font=('arial', 10),
                    width=20, anchor="e", bd=1,
                    pady=10, padx=10).grid(row=9, column=0)
        self.txt_prod_desc = tk.Entry(form_frame, textvariable=self.flight_price,width=30, bd=1)
        self.txt_prod_desc.grid(row=9, column=1)


        button_frame = tk.Frame(prod_frame, pady=20)
        button_frame.pack()
        tk.Button(button_frame, width=10, text="Clear", 
                  command=self.clear_fields).pack(side=tk.LEFT)
        tk.Button(button_frame, width=10, text="Save", 
                  command=self.save).pack(side=tk.LEFT)
        tk.Button(button_frame, width=10, text="Delete", 
                  command=self.delete).pack(side=tk.LEFT)
        tk.Button(button_frame, width=10, text="Load", 
                  command=self.load).pack(side=tk.LEFT)
        
        return prod_frame
    """
    Clears all the fields of the form
    """
    def clear_fields(self):
    

        # Just blank all the fields
            self.flight_id.set("")
            #self.airline_name.set("")
            #self.from_location.set("")
            #self.title.set("") # Do not clear if using dropdown
            #self.to_location.set("")
            #self.depature_time.set("")
            #self.arrival_time.set("")
            self.duration.set("")
            self.total_seats.set("")
            self.flight_price.set("")




            pass
    """
    Save the data displayed on the form to the database
    """
    def save(self):
        

        print("Saving a flight ...")

        # Get the data
        data = self.get_fields() 

        # Validate the data
        valid_data, message = self.validate_fields(data)
        if valid_data:
            if (data['flight_id']==0):
                # If nothing has been entered in employee_id 
                # i.e. its length is zero characters
                print("Calling create() as flight_id is absent")
                self.create(data)
            else:
                print("Calling update() as flight_id is present")
                self.update(data)
                pass
        else:
            message_text = "Invalid fields.\n" + message 
            messagebox.showwarning(self.mb_title_bar, message_text, icon="warning")
            pass
    """
    Get the data entered in the fields of the form
    """
    def get_fields(self):

        emp = {}
        # employee_id is ignored when creating a record
        emp['flight_id'] = self.flight_id.get()
        emp['airline_name'] = self.airline_name.get()
        emp['from_location'] = self.from_location.get()
        emp['to_location'] = self.to_location.get()
        emp['depature_time'] = self.depature_time.get()
        emp['arrival_time'] = self.arrival_time.get()
        emp['duration'] = self.duration.get()
        emp['total_seats'] = self.total_seats.get()
        emp['flight_price'] = self.flight_price.get()


        return emp    
    """
        Validate the data entered in the fields of the form
    """
    def validate_fields(self, data):
           
        # By default set to true, anything wrong will turn it to false   
        valid_data = True 
        # Instantiate an empty list to contain the messages
        message_list = [] 
        # Check for blank fields
        # Do not check employee_id as this is generated by the database
        #if len(data['employee_id']==0:
        #    valid_data = False
        #    message_list.append("employee_id is empty")
        if len(data['airline_name'])==0:
            valid_data = False
            message_list.append("airline_name is empty")
        if len(data['from_location'])==0:
            valid_data = False
            message_list.append("from_location is empty")
        if len(data['to_location'])==0:
            valid_data = False
            message_list.append("to_location is empty")
        if len(str(data['depature_time']))==0:
            valid_data = False
            message_list.append("depature_time is empty")
        if len(str(data['arrival_time']))==0:
            valid_data = False
            message_list.append("arrival_time is empty")
        if len(str(data['duration']))==0:
            valid_data = False
            message_list.append("duration is empty")
        if len(str(data['total_seats']))==0:
            valid_data = False
            message_list.append("total_seats is empty")
        if len(str(data['flight_price']))==0:
            valid_data = False
            message_list.append("flight_price is empty")

           
            
        # Join the items in the list as a string separated with a comma and a space    
        message = ', '.join(message_list) 

        return valid_data, message # return 2 values
    """
     Create a new record in the database.
    """
    def create(self, data): 

        print("Creating a flight ...")
        print(data)

        session = db.get_db_session() # Get a session (database.py)
        result = self.flt_dao.create(session, data) 
          # result is a tuple e.g. ("Employee added successfully", 1004) 
        #result, employee_id = self.emp.create(data) 
          # if you wish to get the message and employee_id separately
        session.close() # Close the session

        messagebox.showinfo(self.mb_title_bar, result)
 
        pass
    """
     Create a new record in the database.
    """
    def update(self, data):
        
        print("Updating flight ...")
        print(data)

        session = db.get_db_session() # Get a session (database.py)
        result = self.flt_dao.update(session, data['flight_id'], data)
        session.close() # close the session

        # Display the returned message to the user - use a messagebox  
        # Display everything that is returned in the result      
        messagebox.showinfo(self.mb_title_bar, result)
        pass
    """
    Delete a record in the database
    """
    def delete(self):

        # Grab the employee_id from the stringvar
        id = self.flight_id.get() 
        print(id)
        
        # Call the data access object to do the job
        # Pass the id as parameter to the delete() method
        session = db.get_db_session() # Get a session (database.py)
        result = self.flt_dao.delete(session, id)
        session.close() # Close the session

        # Display the returned message to the user - use a messagebox    
        # Display everything that is returned in the result    
        messagebox.showinfo(self.mb_title_bar, result)
        pass
    """
    load records in the database
    """    
    def load(self):
        session = db.get_db_session() # Get a session (database.py)
        result = self.flt_dao.find_ids(session) # {"employee_ids": [1, 2, 3]}
        session.close() # Close the session
        print("result", result)
        # Check if there is an entry in the result dictionary
        if "flight_ids" in result: 
            list_ids = result['flight_ids'] 
            self.lb_ids.delete(0,tk.END)
            print("Setting flight_id in listbox ...")
            for x in list_ids:
                self.lb_ids.insert(tk.END, x)
                #print(x)
            pass

    """
    on_list_select() is triggered when a user clicks an item in the listbox.
    """    
    def on_list_select(self, evt):
        """
        on_list_select() is triggered when a user clicks an item in the listbox.
        This was defined with the statement 
        "self.lb_ids.bind('<<ListboxSelect>>', self.on_list_select)" 
        defined above in create_gui()

        Parameters (apart from self):
            evt: object containing information about the mouse click

        Return: None
        """
        # For more information on 'tkinter events', 
        # refer to http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
        w = evt.widget
        index = int(w.curselection()[0]) 
          # index = position of the item clicked in the list, first item is item 0 not 1
        value = w.get(index) 
          # value of the item clicked, in our case it's the employee_id
        print(index) 
        print(value)

        # Call find_by_id and populate the stringvars of the form
        session = db.get_db_session() # Get a session (database.py)
        result = self.flt_dao.find_by_id(session, value)   
        session.close() # close the session
        print("result", result) 
           # { "employee" : {"employee_id": "", "firstname": "", etc}}
        emp = result['flight']
        self.populate_fields(emp)
        pass
    """
    Populate the fields of the form with data
    """
    def populate_fields(self, emp):

        # Set the values from the dict to the stringvars
         self.flight_id.set(emp['flight_id'])
         self.airline_name.set(emp['airline_name'])
         self.from_location.set(emp['from_location'])
         self.to_location.set(emp['to_location'])
         self.depature_time.set(emp['depature_time'])
         self.arrival_time.set(emp['arrival_time'])
         self.duration.set(emp['duration'])
         self.total_seats.set(emp['total_seats'])
         self.flight_price.set(emp['flight_price'])


         pass

# ###########
# Main method
# ###########
"""
    The main method is only executed when the file is 'run' 
    (not imported in another file)
"""
if __name__ == '__main__':
    
    # Setup a root window (in the middle of the screen)
    root = tk.Tk()
    root.title("Procurement System")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 900
    height = 500
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(0, 0)

    # Instantiate the gui
    gui = FlightGUI()

    # Create the gui - pass the root window as parameter
    gui.create_gui(root)

    # Run the mainloop - the endless window loop to process user inputs
    root.mainloop()