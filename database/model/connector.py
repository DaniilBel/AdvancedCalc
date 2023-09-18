import mysql.connector
from mysql.connector import Error


def create_connection():
    """
    Create connection to database.
    """

    try:
        connection = mysql.connector.connect(
            host='db',
            port=3306,
            user='user_name',
            passwd='password',
            database='advanced_calc',
        )
        connection.autocommit = True
        print("Connection to MySQl DB successful")

        return connection
    except Error as err:
        print(f"The error '{err}' occurred")
        raise err
