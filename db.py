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
