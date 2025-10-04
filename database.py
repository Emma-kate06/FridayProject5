import sqlite3
from datetime import date

# 1. Define the database file name
DB_NAME = 'customer_data.db'

def setup_database():
    """Connects to the database and creates the customer table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create the table with the specified fields
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            birthday TEXT,  -- Stored as TEXT in YYYY-MM-DD format
            email TEXT,
            phone_number TEXT,
            address TEXT,
            preferred_contact TEXT CHECK(preferred_contact IN ('email', 'phone', 'mail', 'other'))
        )
    ''')
    conn.commit()
    conn.close()
    print(f"Database '{DB_NAME}' and table 'customers' are ready.")


def insert_customer(name, birthday, email, phone_number, address, preferred_contact):
    """Inserts a new customer record into the database."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # SQL to insert the data
        sql_insert = '''
            INSERT INTO customers (name, birthday, email, phone_number, address, preferred_contact)
            VALUES (?, ?, ?, ?, ?, ?)
        '''
        
        # Data to be inserted (as a tuple)
        data = (name, birthday, email, phone_number, address, preferred_contact)
        
        cursor.execute(sql_insert, data)
        conn.commit()
        print(f"\nSuccessfully inserted customer: {name}")

    except sqlite3.Error as e:
        print(f"\nAn error occurred: {e}")
        
    finally:
        if conn:
            conn.close()


# --- EXECUTION ---

# 2. Run the setup function to create the database/table
setup_database()

# 3. Example of inserting a new customer entry
insert_customer(
    name="Alice Wonderland",
    birthday="1990-05-15",
    email="alice@example.com",
    phone_number="555-123-4567",
    address="10 Tea Party Lane, Fantasyland",
    preferred_contact="email"
)

# 4. Another example insertion
insert_customer(
    name="Bob The Builder",
    birthday="1975-12-01",
    email="bob@buildit.com",
    phone_number="555-987-6543",
    address="20 Tool Box Road, Fixit City",
    preferred_contact="phone"
)

# Optional: You can now query the database to see the records
def view_customers():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    records = cursor.fetchall()
    print("\n--- Current Customers in Database ---")
    for row in records:
        print(row)
    conn.close()

view_customers()