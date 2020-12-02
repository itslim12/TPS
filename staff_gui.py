# employee_gui.py
# France Cheong
# 22/11/2018

# ########
# Packages
# ########
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk # for combobox

# #################################################
# Import any of your classes defined in other files
# #################################################

import database as db # Import database.py to get a session to a particular db
# From file xxx.py import class Xxxx
from staff_dao import StaffDAO # To communicate with Employee table
from validation import Validation # To validate the entries made on the form


# #################
# EmployeeGUI Class
# #################

class StaffGUI():
    """
    GUI class to perform CRUD operations on the employee table in the database.
    """   

    def __init__(self):   
        """
        The initialiser is used to "instantiate" attributes of the class.
        The attributes are the "variables" that have been declared "outside" 
        of the methods of the class.
        Some attributes may have not been declared as they may be created 
        any where in the class methods (python allows this).

        Attributes are like global variables for the class, as they are 
        available to any method in the class.
        And, to use them, they must be prefixed with "self."
        
        This differentiates them from "local" variables which are 
        defined/created and used within a single method

        If you need to pass the value of a local variable from one method 
        to another, then you must pass "parameters" to the method 

        We cannot create the GUI here as we need to return a reference to 
        the frame created.
        Hence, we need to implement a 'normal' function to do this e.g. create_gui()

        Parameters (apart from self): None

        Return: None

        """
    
        # Instantiate a data access object 
        # Contains methods to access the database
        self.emp_dao = StaffDAO()

        # Instantiate a validation object
        # Contains methods to validate input fields
        self.validator = Validation()

        # Form fields
        # Instantiate stringvars - hold  data entered in  fields of form
        self.staff_id = tk.StringVar()
        self.first_name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.title = tk.StringVar()
        self.email = tk.StringVar()
        self.sex = tk.StringVar()
        self.contact_no = tk.IntVar()

        # List of employee ids - lb for listbox
        self.lb_ids = None

        # Messagebox title
        self.mb_title_bar = "Staff CRUD"

        pass 
    
    """
    Create a high level frame which contains the entire GUI 
    """
    def create_gui(self, root):

        
        print("Creating Staff GUI ...")

        
        emp_frame = tk.Frame(root)
        emp_frame.pack()

        
        form_frame = tk.Frame(emp_frame)
        form_frame.pack()
    
        
        tk.Label(form_frame, font=('arial', 10), 
                 text = "Staff").grid(row=0, column=0, columnspan=3)

        # row 1: employee_id label, employee_id entry and list_of_ids label
        tk.Label(form_frame, text= "Staff Id", font=('arial', 10), width=20, 
                 anchor="e", bd=1, pady=10, padx=10).grid(row=1, column=0)
        tk.Entry(form_frame, textvariable=self.staff_id, width=30, bd=1, 
                 state=tk.DISABLED).grid(row=1, column=1)
        tk.Label(form_frame, text= "Staff IDs", 
                 font=('arial', 10)).grid(row=1, column=2)
        
         # row 2: title label and combobox (the listbox will go through)
        tk.Label(form_frame, text= "Title", font=('arial', 10), width=20, 
                 anchor="e", bd=1, pady=10, padx=10).grid(row=2, column=0)
        VALUES = ('Mr','Mrs','Ms', 'Miss', 'Dr')
        ttk.Combobox(form_frame, state="readonly", textvariable=self.title, 
                  values=VALUES, width=10).grid(row=2, column=1, sticky="w")
        self.title.set(VALUES[0]) 
        
        # row 3: firstname label, firstname entry and listbox of ids
        tk.Label(form_frame, text= "First name", font=('arial', 10), 
                 width=20, anchor="e", bd=1, pady=10, padx=10).grid(row=3, column=0)
        tk.Entry(form_frame, textvariable=self.first_name, 
                 width=30, bd=1).grid(row=3, column=1)

        self.lb_ids = tk.Listbox(form_frame)
        self.lb_ids.grid(row=3, column=2, rowspan=5)  
        self.lb_ids.bind('<<ListboxSelect>>', self.on_list_select)

        # row 4: lastname label and entry (the listbox will go through)
        tk.Label(form_frame, text= "Last name", font=('arial', 10), width=20, 
                 anchor="e", bd=1, pady=10, padx=10).grid(row=4, column=0)
        tk.Entry(form_frame, textvariable=self.last_name, 
                 width=30, bd=1).grid(row=4, column=1)

        # row 5: title label and combobox (the listbox will go through)
        tk.Label(form_frame, text= "Sex", font=('arial', 10), width=20, 
                 anchor="e", bd=1, pady=10, padx=10).grid(row=5, column=0)
        VALUES = ('Male','Female','Undefined')
        ttk.Combobox(form_frame, state="readonly", textvariable=self.sex, 
                  values=VALUES, width=10).grid(row=5, column=1, sticky="w")
        
        # row 6: email label and combobox (the listbox will go through)
        tk.Label(form_frame, text= "Email", font=('arial', 10), 
                 width=20, anchor="e", bd=1, pady=10, padx=10).grid(row=6, column=0)
        tk.Entry(form_frame, textvariable=self.email, width=30, bd=1).grid(row=6, column=1)

        # row 7: work_phone label and combobox (the listbox will go through)
        tk.Label(form_frame, text= "Contact No", font=('arial', 10), width=20, 
                 anchor="e", bd=1, pady=10, padx=10).grid(row=7, column=0)
        tk.Entry(form_frame, textvariable=self.contact_no, 
                 width=30, bd=1).grid(row=7, column=1)

        # Buttons

        button_frame = tk.Frame(emp_frame, pady=10) 
        button_frame.pack()
        
        tk.Button(button_frame, width=10, text="Clear", 
                  command=self.clear_fields).pack(side=tk.LEFT)
        tk.Button(button_frame, width=10, text="Save", 
                  command=self.save).pack(side=tk.LEFT)
        tk.Button(button_frame, width=10, text="Delete", 
                  command=self.delete).pack(side=tk.LEFT)
        tk.Button(button_frame, width=10, text="Load", 
                  command=self.load).pack(side=tk.LEFT)       

        # Return a reference to the high level frame created
        return emp_frame

    """
    Clears all the fields of the form
    """
    def clear_fields(self):

        self.staff_id.set("")
        self.first_name.set("")
        self.last_name.set("")
        #self.sex.set("") # Do not clear if using dropdown
        #self.title.set("") # Do not clear if using dropdown
        self.email.set("")
        self.contact_no.set("")
        pass

    """
    Save the data displayed on the form to the database
    """
    def save(self):

        print("Saving staff....")

        # Get the data
        data = self.get_fields()   

        # Validate the data
        valid_data, message = self.validate_fields(data)
        if valid_data:
            if (len(data['staff_id'])==0):
                # If nothing has been entered in employee_id 
                # i.e. its length is zero characters
                print("Calling create() as staff_id is absent")
                self.create(data)
            else:
                print("Calling update() as staff_id is present")
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
        emp['staff_id'] = self.staff_id.get() 
        emp['first_name'] = self.first_name.get()
        emp['last_name'] = self.last_name.get()
        emp['title'] = self.title.get()
        emp['sex'] = self.sex.get()
        emp['email'] = self.email.get()
        emp['contact_no'] = self.contact_no.get()

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
        if len(str(data['first_name']))==0:
            valid_data = False
            message_list.append("first_name is empty")
        if len(str(data['last_name']))==0:
            valid_data = False
            message_list.append("last_name is empty")
        if len(data['title'])==0:
            valid_data = False
            message_list.append("title is empty")
        if len(data['sex'])==0:
            valid_data = False
            message_list.append("sex is empty")
        if len(str(data['email']))==0:
            valid_data = False
            message_list.append("work_phone is empty")
        if len(str(data['contact_no']))==0:
            valid_data = False
            message_list.append("contact_no is empty")

        if not self.validator.is_alphabetic(data['first_name']):
            valid_data = False
            message_list.append("invalid first_name")

        if not self.validator.is_alphabetic(data['last_name']):
            valid_data = False
            message_list.append("invalid last_name")
    
        # Check if title is in a list [Mr, Ms, Mrs, Dr, etc]
        if self.title.get() not in ["Mr", "Ms", "Mrs", "Miss", "Dr"]:
            valid_data = False
            message_list.append("title should be Mr, Ms, Mrs, Miss or Dr")

        # Check if email follows a certain pattern 
        # i.e contains an @ followed by a dot
        if not self.validator.is_email(data['email']):
            valid_data = False
            message_list.append("invalid email format")

        # Join the items in the list as a string separated with a comma and a space    
        message = ', '.join(message_list) 

        return valid_data, message # return 2 values

    """
     Create a new record in the database.
    """
    def create(self, data):

        print("Creating an staff ...")
        print(data)

        session = db.get_db_session() # Get a session (database.py)
        result = self.emp_dao.create(session, data) 
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
       
        print("Updating staff ...")
        print(data)

        session = db.get_db_session() # Get a session (database.py)
        result = self.emp_dao.update(session, data['staff_id'], data)
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
        id = self.staff_id.get() 
        print(id)
        
        # Call the data access object to do the job
        # Pass the id as parameter to the delete() method
        session = db.get_db_session() # Get a session (database.py)
        result = self.emp_dao.delete(session, id)
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
        result = self.emp_dao.find_ids(session) # {"employee_ids": [1, 2, 3]}
        session.close() # Close the session
        print("result", result)
        # Check if there is an entry in the result dictionary
        if "staff_ids" in result: 
            list_ids = result['staff_ids'] 
            self.lb_ids.delete(0,tk.END)
            print("Setting staff_id in listbox ...")
            for x in list_ids:
                self.lb_ids.insert(tk.END, x)
                #print(x)
            pass
    """
    on_list_select() is triggered when a user clicks an item in the listbox.
    """ 
    def on_list_select(self, evt):
     
        w = evt.widget
        index = int(w.curselection()[0]) 
          # index = position of the item clicked in the list, first item is item 0 not 1
        value = w.get(index) 
          # value of the item clicked, in our case it's the employee_id
        print(index) 
        print(value)

        # Call find_by_id and populate the stringvars of the form
        session = db.get_db_session() # Get a session (database.py)
        result = self.emp_dao.find_by_id(session, value)   
        session.close() # close the session
        print("result", result) 
           # { "employee" : {"employee_id": "", "firstname": "", etc}}
        emp = result['staff']
        self.populate_fields(emp)
        pass
    """
    Populate the fields of the form with data
    """
    def populate_fields(self, emp):
    
        # Set the values from the dict to the stringvars
        self.staff_id.set(emp['staff_id'])
        self.first_name.set(emp['first_name'])
        self.last_name.set(emp['last_name'])
        self.title.set(emp['title'])
        self.sex.set(emp['sex'])
        self.email.set(emp['email'])
        self.contact_no.set(emp['contact_no'])
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
    gui = StaffGUI()

    # Create the gui
    # pass the root window as parameter
    gui.create_gui(root)

    # Run the mainloop 
    # the endless window loop to process user inputs
    root.mainloop()
    pass