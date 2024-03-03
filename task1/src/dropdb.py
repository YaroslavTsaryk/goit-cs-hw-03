import psycopg2

conn = psycopg2.connect(
    database="postgres", user="postgres", host="localhost", password="567234", port=5432
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: drop users table
cur.execute(
    """drop TABLE if exists users;
            """
)
# Make the changes to the database persistent
conn.commit()

# Execute a command: drop status table
cur.execute(
    """DROP TABLE if exists status;
            """
)
# Make the changes to the database persistent
conn.commit()


# Execute a command: drop tasks table
cur.execute(
    """DROP TABLE if exists tasks;
            """
)
# Make the changes to the database persistent
conn.commit()


# Close cursor and communication with the database
cur.close()
conn.close()
