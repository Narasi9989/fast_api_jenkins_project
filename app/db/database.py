import oracledb
oracledb.init_oracle_client(lib_dir=r"C:\instantclient-basic-windows.x64-23.26.2.0.0\instantclient_23_0")

def get_connection():
    connection = oracledb.connect(
    user="narasimha",
    password ="narasimha",
    dsn="localhost:1521/XE"
)

    return connection
    


print("Connected")