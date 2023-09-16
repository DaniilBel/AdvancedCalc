from mysql.connector import Error
from typing import List, Optional

from model.calc_history import History, History_get
from model.connector import create_connection


class HistoryRepository:
    """
    The class executes API logic for history.
    """

    def __init__(self):
        self.connection = create_connection()


    def add_history(self, history: History) -> Optional[str]:
        """
        This method creates and adds new history in table.
        """
        
        cursor = self.connection.cursor()
        query = """
        INSERT INTO calc_history (line, answer) 
        VALUES (%s, %s)
        """

        try:
            cursor.execute(query, [history.line, 
                                   history.answer])
            cursor.close()
            return "History line add successfully."
        except Error as err:
            return None
    
    # other methods
