# FridayProject5

📊 Customer Data Management System
This repository contains a simple Python application designed to collect customer information via a Graphical User Interface (GUI) and store it persistently using an SQLite database. It also includes an administrative script for easy data viewing.

📁 File Structure and Overview
This project is composed of one database file, three Python scripts, and two markdown documentation files.

File Name

Purpose

customer_data.db

The central database file. This SQLite file stores all customer information submitted through the GUI.

databaseGUI.py

The primary user-facing application. This script runs the GUI that allows customers to enter their details and submit them to the database.

readDatabase.py

The administrative utility. This script connects to customer_data.db, reads all stored data, and displays it directly in the console.

database.py

The foundational script. This file was used for the initial creation and setup of the database structure and table definitions.

Friday Project 5.md

Documentation file containing the instructions, requirements, and background notes for this project.

README.md

This file, providing an overview of the project and file usage.

🚀 Usage
1. Data Submission (Customer View)
To launch the customer entry interface, run the GUI file:

python databaseGUI.py

This will open the application where customers can input their data and press "Submit" to save the information to customer_data.db.

2. Data Viewing (Administrator View)
To quickly view all the data currently stored in the database, run the readDatabase.py file:

python readDatabase.py

This script will print all customer records directly to your terminal..