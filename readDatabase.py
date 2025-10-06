import sqlite3

def view_customer_data(database_file="customer_data.db", table_name="customers"):
    """
    Connects to the SQLite database, fetches all records from the specified
    table, and prints them to the console.

    Args:
        database_file (str): The name of the SQLite database file.
        table_name (str): The name of the table to query.
    """
    conn = None # Initialize connection to None
    try:
        # 1. Connect to the SQLite database file
        conn = sqlite3.connect(database_file)
        cursor = conn.cursor()

        # 2. Execute a SQL query to select all data from the table
        # NOTE: Replace 'customers' with your actual table name if it's different.
        print(f"--- Data from '{table_name}' table ---")
        cursor.execute(f"SELECT * FROM {table_name}")

        # 3. Fetch all the results
        all_rows = cursor.fetchall()

        # 4. Print the fetched data
        if all_rows:
            # Optional: Get column names (schema) for better display
            column_names = [description[0] for description in cursor.description]
            print(" | ".join(column_names))
            print("-" * (sum(len(c) for c in column_names) + len(column_names) * 3)) # Simple separator

            for row in all_rows:
                # Assuming data are strings or can be easily converted to strings
                print(" | ".join(map(str, row)))
        else:
            print("The table is empty or the table/database was not found.")

    except sqlite3.Error as e:
        # Handle potential errors (e.g., file not found, table not found, bad SQL)
        print(f"An error occurred: {e}")

    finally:
        # 5. Close the database connection (important!)
        if conn:
            conn.close()
            print("\nDatabase connection closed.")

if __name__ == "__main__":
    # Call the function to view the data.
    # Replace 'customers' with your actual table name if it's something else!
    view_customer_data(table_name="customers")