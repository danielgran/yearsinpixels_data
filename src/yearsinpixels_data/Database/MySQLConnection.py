from mysql.connector import connect


class MySQLConnection:
    def __init__(self):
        self.connected = False
        self.password = ""
        self.host = "localhost"
        self.port = 3306
        self.database = ""
        self.username = ""
        self.connection = None

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
        if self.connection.connection_id is None:
            return False
        return True
