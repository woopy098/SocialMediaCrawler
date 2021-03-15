import mysql.connector
from mysql.connector import Error

class Database:

    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "password" #change if password is different
        self.database = "sqldatabase" #change if different database
        self.charset = "utf8mb4" #
        self._connection() #call _connection function

    def _connection(self):
        try:
            conn = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database,
                charset = self.charset
            )
            self._db = conn
        except Error as err:
            print("error while connecting to database",err)

    def createTable(self): #not required anymore as the database is inside .sql script
        cursor = self._db.cursor()
        #cursor.execute(("CREATE TABLE IF NOT EXISTS commenteds(category VARCHAR(50) NOT NULL,user VARCHAR(20) NOT NULL,commentedd VARCHAR(5000) NOT NULL)")) #checked
        #id INT NOT NULL AUTO_INCREMENT
        self._db.commit() #to update database
        cursor.close()
        #self._disconnect()
        #print ("table created")
        pass

    def disconnect(self): # put _ to make it private
        self._db.close()
        print("connection close")

    def insert(self, cid, user, comment, datecreate): # change to 4parameter
        #enter whatever or grab whatever put inside here to insert
        cursor = self._db.cursor() #access sql
        val = (cid, user,comment,datecreate)
        print(val)
        cursor.execute("INSERT INTO comment (cid,user,comments,dates) VALUES (%s, %s,%s,%s)", val)
        self._db.commit() #update database
        #print("record inserted.")
        cursor.close() #close cursor everytime after use for security purposes

    def update(self):
        cursor = self._db.cursor()
        #updating code here
        cursor.close()
        pass

    def read(self):
        cursor = self._db.cursor()
        #self._connection()
        cursor.execute("SELECT * FROM comment") #select all from table(comment)
        result = cursor.fetchall()
        # for x in result:
        #     print(x)
        cursor.close()
        return result

    def update(self):
        cursor = self._db.cursor()
        #codes
        cursor.close()
        pass

    def delete(self):
        cursor = self._db.cursor()
        #codes
        cursor.close()
        pass

    def truncatetable(self):
        cursor = self._db.cursor()
        cursor.execute("TRUNCATE TABLE comment")  # THIS IS TO REMOVE ITEM FROM THE TABLE SAVED PREVIOUSLY
        # updating code here
        cursor.close()
