import mysql.connector
import pandas as pd

class MySQLConnector:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Connected to MySQL database")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def fetch_all_data(self, table):
        try:
            query = f"SELECT * FROM {table}"
            self.cursor.execute(query)
            columns = [column[0] for column in self.cursor.description]
            data = self.cursor.fetchall()
            df = pd.DataFrame(data, columns=columns)
            return df
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def disconnect(self):
        try:
            self.cursor.close()
            self.connection.close()
            print("Disconnected from MySQL database")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

def StartImport():
    # MySQL database connection details
    host = 'localhost'
    user = 'root'
    password = '2023'
    database = 'Agri'

    # Create MySQLConnector object
    mysql_connector = MySQLConnector(host, user, password, database)

    # Connect to the MySQL database
    mysql_connector.connect()

    # Fetch all data from the 'data' table
    agri_data = mysql_connector.fetch_all_data('data')

    # Save the fetched data to a CSV file
    agri_data.to_csv('notebooks/data/agri.csv', index=False)

    # Disconnect from the MySQL database
    mysql_connector.disconnect()
    print("Data Import Completed")

if __name__ == "__main__":
    StartImport()
