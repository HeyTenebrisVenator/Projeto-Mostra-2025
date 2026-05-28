# Database created with XAMPP

# user: 'root'
# password: ''

# default query: INSERT INTO `science_fair_results` (`CreatedAt`, `Url`) VALUES (current_timestamp(), 'URL_GOES_HERE');

# database: ScienceFair
# table: science_fair_results

import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def save_in_db(query):
    try:
        cnx = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST', '127.0.0.1'),
            user=os.getenv('MYSQL_USER', 'root'),
            password=os.getenv('MYSQL_PASSWORD', ''),
            database=os.getenv('MYSQL_DATABASE', 'ScienceFair')
        )
        print("Connection successful!")

        cursor = cnx.cursor()
        cursor.execute(query)

        cnx.commit()  # Essential for saving the insert.
        print("Insert completed successfully!")

    except mysql.connector.Error as err:
        print(f"An error occurred: {err}")

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'cnx' in locals() and cnx.is_connected():
            cnx.close()
            print("Closing the database connection!")
