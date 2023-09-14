import mysql.connector
from mysql.connector import Error


def create_connection():
    """
    Crate connection to database.
    """

    connection = None
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='processionLF0112358.',
            database='advanced_calc',
        )
        connection.autocommit = True
        print("Connection to MySQl DB successful")
    except Error as err:
        print(f"The error '{err}' occerred")
        raise err
    
    return connection
