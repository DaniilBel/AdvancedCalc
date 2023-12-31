from typing import Optional

from mysql.connector import Error

from database.model.calc_history import History
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
        INSERT INTO calc_history (line, answer, is_ans_int, date) 
        VALUES (%s, %s, %s, %s)
        """
        try:
            cursor.execute(query, [history.line,
                                   history.answer,
                                   history.is_ans_int,
                                   history.date])
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

    def get_history(self) -> Optional[list]:
        """
        This method returns the calculation history.
        """

        cursor = self.connection.cursor()
        query = "SELECT * FROM calc_history ORDER BY date DESC"

        try:
            history = []
            cursor.execute(query)

            for row in cursor.fetchall():
                line, answer, is_ans_int, date = row
                history.append([line, (int(answer) if is_ans_int and answer < 1e+12 else answer), is_ans_int, date])
            cursor.close()
            return history

        except Error as err:
            return None
