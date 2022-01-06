from mysql.connector import connect


class MySQLConnection:
    def __init__(self, host="localhost", port=3306, database="", username="", password=""):
        self.host = host
        self.port = port
        self.database = database
        self.username = username
        self.password = password

        self.connection = None
        self.connected = False

    def connect(self):
        self.connection = connect(user=self.username, password=self.password, host=self.host, port=self.port,
                                  database=self.database)
        cursor = self.connection.cursor()
        cursor.execute("SET NAMES utf8mb4")
        cursor.execute("SET CHARACTER SET utf8mb4")
        cursor.execute("SET character_set_connection=utf8mb4")
        self.connection.commit()
        cursor.close()
        self.connection.autocommit = True
        self.connected = True

    def disconnect(self):
        self.connection.disconnect()

    @property
    def is_connected(self):
        return self.connection.is_connected()

    def query(self, query, *args):
        if not self.is_connected:
            self.connect()
        cursor = self.connection.cursor(dictionary=True)
        if len(args) == 0:
            cursor.execute(query)
        else:
            cursor.execute(query, *args)
        rows = list()
        for entity in cursor:
            rows.append(entity)
        cursor.close()
        self.connection.commit()
        return rows
