import pandas as pd
import mysql.connector
from mysql.connector import Error
from transform import transform_news


# Connect to the Neon MySQL server
def create_connection():
    """ Establish connection to Neon MySQL database """
    try:
        connection = mysql.connector.connect(
            host="neon-mysql",  
            user="admin",        
            password="admin",     
            database="news_data"      
        )
        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Function to upload DataFrame to Neon MySQL
def upload_dataframe_to_mysql(df, connection):
    """ Upload Pandas DataFrame to Neon MySQL database """
    cursor = connection.cursor()

    # Create table if it doesn't exist (you can modify this as per your data structure)
    table_creation_query = """
    CREATE TABLE IF NOT EXISTS transformed_data (
        source_name varchar(100),
        author varchar(100),
        title varchar(max),
        description varchar(max),
        url varchar(max),
        published_date date,
        published_time time,
        web_address varchar(50)
    )
    """
    cursor.execute(table_creation_query)

    # Insert DataFrame data into the table
    for i, row in df.iterrows():
        insert_query = """
        INSERT INTO transformed_data (source_name, author, title, description, url, published_date, published_time, web_address)
        VALUES (%s, %s,%s, %s,%s, %s,%s, %s)
        """
        cursor.execute(insert_query, tuple(row))

    # Commit the transaction
    connection.commit()
    print(f"{len(df)} rows inserted successfully into 'transformed_data' table.")
    
    # Close the cursor and connection
    cursor.close()
    connection.close()

# Main script
if __name__ == "__main__":
    # Create connection to the Neon MySQL server
    connection = create_connection()
