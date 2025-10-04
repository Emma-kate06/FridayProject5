# Friday Project 5: Customer Information Management System

**Overview**

For this assignment, you will create a customer information management application that combines a database with a graphical user interface (GUI). This application will allow customers to submit their personal information, which will be stored in a database. This assignment will help you practice database management and GUI design in application development.

**Requirements**

1. **Database Creation for Customer Information**
   - Create a database file to store customer information.
   - Each entry should include the customer's name, birthday, email, phone number, address, and preferred contact method.

2. **GUI Design**
   - Design a graphical user interface (GUI) that customers can interact with.
   - The GUI should have input fields for the customer's name, birthday, email, phone number, address, and a dropdown menu for preferred contact method.
   - Add a **Submit** button that allows customers to submit their information, which should then be stored in the database and clear the form.

**High-Level Instructions**

1. **Set Up the Database**:
   - Use a simple database file (like SQLite) to store the customer data.
   - Ensure that each entry includes fields for the name, birthday, email, phone number, address, and preferred contact method.

2. **Create the GUI**:
   - Use a library (e.g., Tkinter for Python) to build a GUI with input fields for all required customer information.
   - Include a dropdown menu for the preferred contact method (options should include Email, Phone, and Mail).
   - Add a "Submit" button that, when clicked, stores the input data into the database and clears the form for the next entry.

**Additional Tips**

- **Database**: SQLite is a good choice for a lightweight database and is relatively easy to set up.
- **GUI Library**: Tkinter (Python) is recommended for creating the interface.
- **Data Validation**: Consider implementing validation for email formats, date formats, and ensuring required fields are completed.
- **Form Clearing**: Make sure your submit functionality both saves the data AND clears the form for the next customer entry.