import pyodbc,csv

# Replace placeholders with your actual credentials and connection details
server = 'subhrojeets-agriculture.database.windows.net'
port = 1433  # Standard SQL Server port
database = 'AgriData'
username = 'root-subhrojeet'
password = 'SpaceMonkey@123'  # Replace with your actual password

# Construct the connection string using f-strings for clarity
conn_string = f"""
DRIVER={{ODBC Driver 17 for SQL Server}};
SERVER={server},{port};
DATABASE={database};
UID={username};
PWD={password};
"""


# try:
#     # Establish connection using pyodbc.connect
#     connection = pyodbc.connect(conn_string)

#     # Create a sample table (replace 'Customer' with your desired name)
#     cursor = connection.cursor()
#     # Check if the table exists
#     # Check if the table exists
#     table_check_query = """
#             CREATE TABLE Customer (
#                 id INT PRIMARY KEY IDENTITY(1,1),
#                 name VARCHAR(50) NOT NULL,
#                 age INT
#             );

#     """

#     cursor.execute(table_check_query)

#     connection.commit()  # Commit changes to persist the table

#     # Insert sample data (replace values as needed)
#     insert_data_query = """
#         INSERT INTO Customer (name, age) VALUES (?, ?)
#     """
#     cursor.execute(insert_data_query, ('John Doe', 30))
#     cursor.execute(insert_data_query, ('Jane Smith', 25))
#     connection.commit()  # Commit changes to persist the data

#     # Fetch data from the table
#     cursor.execute("SELECT * FROM Customer;")
#     rows = cursor.fetchall()

#     # Print retrieved data
#     print("Fetched Customer Data:")
#     for row in rows:
#         print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")

#     # Close resources (important for proper connection management)
#     cursor.close()
#     connection.close()
#     print("Connected to SQL Server, table created, data inserted, and data fetched successfully!")

# except pyodbc.Error as ex:
#     print("Error connecting to SQL Server:", ex)



try:
    # Establish connection using pyodbc.connect
    connection = pyodbc.connect(conn_string)
    cursor = connection.cursor()

    # Create a table
    create_table_query = """
        IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'AgricultureData')
        BEGIN
            CREATE TABLE AgricultureData (
                State VARCHAR(50),
                District VARCHAR(50),
                Crop VARCHAR(50),
                Year VARCHAR(50),
                Season VARCHAR(50),
                Area FLOAT,
                AreaUnits VARCHAR(50),
                Production FLOAT,
                ProductionUnits VARCHAR(50),
                Yield FLOAT
            );
            COMMIT;
        END
    """
    cursor.execute(create_table_query)

    # Open the CSV file and read its contents
    with open('agri.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            # Insert data into the table
            print(row)
            cursor.execute("""
                INSERT INTO AgricultureData (State, District, Crop, Year, Season, Area, AreaUnits, Production, ProductionUnits, Yield)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, row)
        connection.commit()  # Commit changes to persist the data

    print("Table created and data imported successfully!")

except pyodbc.Error as ex:
    print("Error connecting to SQL Server:", ex)