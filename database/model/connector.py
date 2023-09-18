import mysql.connector
from mysql.connector import Error


def create_connection():
    """
    Create connection to database.
    """

    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            # passwd='processionLF0112358.',
            passwd='1234',
            database='advanced_calc',
        )
        connection.autocommit = True
        print("Connection to MySQl DB successful")

        return connection
    except Error as err:
        print(f"The error '{err}' occurred")
        raise err
