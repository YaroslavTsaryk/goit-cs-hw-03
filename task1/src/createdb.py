import psycopg2

conn = psycopg2.connect(
    database="postgres", user="postgres", host="localhost", password="567234", port=5432
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: create users table
cur.execute(
    """CREATE TABLE if not exists users(
            id SERIAL PRIMARY KEY,
            fullname VARCHAR (100) UNIQUE NOT NULL,
            email VARCHAR (100) UNIQUE NOT NULL);
            """
)
# Make the changes to the database persistent
conn.commit()

# Execute a command: create status table
cur.execute(
    """CREATE TABLE if not exists status(
            id SERIAL PRIMARY KEY,
            name VARCHAR (50) UNIQUE NOT NULL);
            """
)
# Make the changes to the database persistent
conn.commit()


# Execute a command: create tasks table
cur.execute(
    """CREATE TABLE if not exists tasks(
            id SERIAL PRIMARY KEY,
            title VARCHAR (100) NOT NULL,
            description TEXT NOT NULL,         
            status_id INT,
            user_id INT,   
            FOREIGN KEY (status_id) REFERENCES status (id)
                ON DELETE SET NULL
                ON UPDATE CASCADE,
            FOREIGN KEY (user_id) REFERENCES users (id)
                ON DELETE CASCADE
                ON UPDATE CASCADE);
            """
)
# Make the changes to the database persistent
conn.commit()

# Close cursor and communication with the database
cur.close()
conn.close()
