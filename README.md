# Medication Maven - HackRX Project

Medication Maven is an application demo developed as part of the HackRX hackathon. It is designed to help users manage their medication schedule by providing reminders and tracking their medication intake.

## Features

- User authentication: Users can log in to access their personalized medication schedule.
- Medication reminders: Users can view their medication reminders and set intervals for taking medications.
- Reminder sound and check-off: Reminders play a sound when it's time to take the medication, and users can check off when they've taken it.
- Dashboard: Users can access the dashboard to view their medication schedule and access other functions.
- MySQL database integration: User information and medication reminders are stored in a MySQL database for persistence.

## Technologies Used

- Python
- PySimpleGUI for GUI development
- MySQL database for data storage
- MySQL Connector/Python for connecting Python to MySQL

## Setup and Installation

1. Clone the repository:

   git clone https://github.com/your-username/hackrx-medication-maven.git

2. Install the required dependencies:

  pip install PySimpleGUI mysql-connector-python

3. Set up the MySQL database:

  - Ensure that you have MySQL installed and running.
  - Create a new database named medication_maven.

4. Update the database connection details:

  - Open db.py and modify the host, user, password, and database variables             according to your MySQL configuration.

## Run the application:

python index.py

## Usage

1. Launch db.py and insert a login into the database users table
2. Launch the application (index.py).
3. Log in using your username and password.
4. The dashboard lets you view your medication schedule and access various         functions.
5. Click on the "Reminder" button to open the reminder section.
6. In the reminder section, you can view your existing medication reminders and       add new ones.
7. Each reminder will play a sound when it's time to take the medication, and you     can check it off once taken.
