import tkinter as tk
from tkinter import messagebox
import sqlite3

# --- Database Configuration ---
DB_NAME = 'database.py'

def setup_database():
    """Connects to the database and creates the customer table if it doesn't exist."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Define the table schema matching the previous request
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                birthday TEXT,  -- Stored as TEXT in YYYY-MM-DD format
                email TEXT,
                phone_number TEXT,
                address TEXT,
                preferred_contact TEXT
            )
        ''')
        conn.commit()
        return conn
        
    except sqlite3.Error as e:
        # If database creation fails, show an error and return None
        messagebox.showerror("Database Error", f"Could not set up database: {e}")
        return None
        
    finally:
        # Ensure the connection is closed if it wasn't returned
        if 'conn' in locals() and conn:
            conn.close()

class CustomerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Customer Data Entry")
        self.geometry("600x450")
        self.configure(bg="#f4f7f9")

        # Set up database connection (will be connected/closed during submit)
        setup_database()

        # --- Variables to hold form data ---
        self.name_var = tk.StringVar()
        self.birthday_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.address_var = tk.StringVar()
        
        # Variable for the Dropdown/Option Menu
        self.contact_options = ['Email', 'Phone', 'Mail']
        self.contact_var = tk.StringVar(value=self.contact_options[0]) # Default value
        
        # --- Build the UI ---
        self.create_widgets()

    def create_widgets(self):
        # Configure a main frame for structure and padding
        main_frame = tk.Frame(self, padx=20, pady=20, bg="#ffffff", relief=tk.RAISED, bd=1)
        main_frame.pack(pady=30, padx=30, fill="both", expand=True)

        # Configure grid column weights for responsive layout
        main_frame.grid_columnconfigure(1, weight=1)
        
        # --- Form Fields ---
        
        fields = [
            ("Name:", self.name_var),
            ("Birthday (YYYY-MM-DD):", self.birthday_var),
            ("Email:", self.email_var),
            ("Phone Number:", self.phone_var),
            ("Address:", self.address_var)
        ]
        
        row_idx = 0
        for label_text, variable in fields:
            # Label
            tk.Label(main_frame, text=label_text, bg="#ffffff", anchor="w", font=('Inter', 10, 'bold'))\
                .grid(row=row_idx, column=0, sticky="w", pady=5, padx=10)
            
            # Entry Field
            tk.Entry(main_frame, textvariable=variable, width=40, bd=1, relief=tk.SUNKEN, font=('Inter', 10))\
                .grid(row=row_idx, column=1, sticky="ew", pady=5, padx=10)
            
            row_idx += 1

        # --- Preferred Contact Dropdown ---
        tk.Label(main_frame, text="Preferred Contact:", bg="#ffffff", anchor="w", font=('Inter', 10, 'bold'))\
            .grid(row=row_idx, column=0, sticky="w", pady=5, padx=10)

        # Dropdown menu (OptionMenu)
        contact_menu = tk.OptionMenu(main_frame, self.contact_var, *self.contact_options)
        contact_menu.config(width=15, bd=1, relief=tk.RAISED, bg="#e0e6ed", activebackground="#c5ccd3", font=('Inter', 10))
        contact_menu.grid(row=row_idx, column=1, sticky="w", pady=5, padx=10)
        
        row_idx += 1

        # --- Submit Button ---
        submit_button = tk.Button(main_frame, text="Submit & Clear Form", command=self.submit_data, 
                                  bg="#4c77af", fg="white", font=('Inter', 11, 'bold'), 
                                  activebackground="#3e6393", activeforeground="white", 
                                  padx=15, pady=8, bd=0, relief=tk.RIDGE)
        submit_button.grid(row=row_idx, column=0, columnspan=2, pady=25)


    def submit_data(self):
        """Validates input, inserts data into the database, and clears the form."""
        
        # 1. Collect Data
        data = {
            'name': self.name_var.get().strip(),
            'birthday': self.birthday_var.get().strip(),
            'email': self.email_var.get().strip(),
            'phone_number': self.phone_var.get().strip(),
            'address': self.address_var.get().strip(),
            'preferred_contact': self.contact_var.get().strip()
        }

        # Simple validation: ensure name is not empty
        if not data['name']:
            messagebox.showwarning("Input Error", "The customer Name field cannot be empty.")
            return

        conn = None
        try:
            # 2. Open Connection
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()

            # 3. Prepare and Execute SQL Insertion
            sql_insert = '''
                INSERT INTO customers (name, birthday, email, phone_number, address, preferred_contact)
                VALUES (?, ?, ?, ?, ?, ?)
            '''
            
            # Data tuple, ensure the order matches the SQL query above
            data_tuple = (
                data['name'], 
                data['birthday'], 
                data['email'], 
                data['phone_number'], 
                data['address'], 
                data['preferred_contact']
            )
            
            cursor.execute(sql_insert, data_tuple)
            conn.commit()

            # 4. Success Feedback and Form Clear
            messagebox.showinfo("Success", f"Customer '{data['name']}' submitted successfully!")
            self.clear_form()

        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Failed to insert data: {e}")
            
        finally:
            # 5. Close Connection
            if conn:
                conn.close()

    def clear_form(self):
        """Resets all input fields to their default state."""
        self.name_var.set("")
        self.birthday_var.set("")
        self.email_var.set("")
        self.phone_var.set("")
        self.address_var.set("")
        # Reset dropdown to the first option
        self.contact_var.set(self.contact_options[0]) 

if __name__ == "__main__":
    app = CustomerApp()
    app.mainloop()