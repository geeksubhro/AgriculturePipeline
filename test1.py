import os
# os.environ["AZURE_SQL_CONNECTIONSTRING"] = "Driver={ODBC Driver 18 for SQL Server};Server=tcp:subhrojeets-agriculture.database.windows.net,1433;Database=AgriData;UID=root-subhrojeet;PWD=SpaceMonkey@123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30"
print(os.environ.get("AZURE_SQL_CONNECTIONSTRING"))
connection_string = os.getenv("AZURE_SQL_CONNECTIONSTRING")
print(connection_string)
print(os.environ["AZURE_SQL_CONNECTIONSTRING"])

# set AZURE_SQL_CONNECTIONSTRING = "Driver={ODBC Driver 18 for SQL Server};Server=tcp:subhrojeets-agriculture.database.windows.net,1433;Database=AgriData;UID=root-subhrojeet;PWD=SpaceMonkey@123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30"