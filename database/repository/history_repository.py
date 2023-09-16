from mysql.connector import Error
from typing import Optional

from database.model.calc_history import History, History_get
from database.model.connector import create_connection


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


    def clear_history(self) -> Optional[str]:
        """
        This method clears history.
        """

        cursor = self.connection.cursor()
        query = """TRUNCATE TABLE calc_history"""

        try:
            cursor.execute(query)
            cursor.close()
            return "History cleared."

        except Error as err:
            return None


    def get_answer(self, line: str) -> Optional[History_get]:
        """
        This method returns the historical calculation response.
        """

        cursor = self.connection.cursor()
        query = f"""
        SELECT * FROM calc_history
        WHERE line='{line}'
        LIMIT 1
        """

        try:
            cursor.execute(query)
            line, answer = cursor.fetchall()[0]
            cursor.close()
            return History_get(line, answer)

        except Error as err:
            return None


    def get_history(self) -> Optional[list]:
        """
        This method returns the calculation history.
        """

        cursor = self.connection.cursor()
        query = "SELECT * FROM calc_history"

        try:
            history = []
            cursor.execute(query)

            for row in cursor.fetchall():
                line, answer = row
                #history.append(History_get(line, answer))
                history.append([line, answer])

            cursor.close()
            return history

        except Error as err:
            return None
