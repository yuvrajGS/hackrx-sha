import mysql.connector

# Connect to the MySQL server
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yuvraj",
    database="medication_maven"
)
# Create the database
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS medication_maven")
db.database = "medication_maven"

# Create the 'users' table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) UNIQUE,
        password VARCHAR(50)
    )
""")

# Create the 'reminders' table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS reminders (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        medication_name VARCHAR(100),
        interval_hours INT,
        description VARCHAR(255),
        taken BOOLEAN DEFAULT 0,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
""")

# Commit the changes
db.commit()

def get_reminders(user_id):
    cursor = db.cursor()
    cursor.execute("SELECT medication_name, interval_hours, description, taken FROM reminders WHERE user_id = %s", (user_id,))
    reminders = cursor.fetchall()
    return reminders

def store_reminder(user_id, medication_name, interval_hours, description):
    cursor = db.cursor()
    cursor.execute("INSERT INTO reminders (user_id, medication_name, interval_hours, description) VALUES (%s, %s, %s, %s)", (user_id, medication_name, interval_hours, description))
    db.commit()
