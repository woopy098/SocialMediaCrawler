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
        cursor.execute("CREATE TABLE crawleddata (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, type VARCHAR(20) COLLATE utf8mb4_unicode_ci NOT NULL,user VARCHAR(100) COLLATE utf8mb4_unicode_ci NOT NULL,"
                       "text VARCHAR(10000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL NULL,"
                       "likes INT , dates DATETIME , commented INT )")
        #id INT NOT NULL AUTO_INCREMENT
        self._db.commit() #to update database
        cursor.close()
        pass

    def disconnect(self): # put _ to make it private
        self._db.close()
        print("connection close")

    def insert(self, type, user, text,likes,datecreate,commented): # change to 4parameter
        #enter whatever or grab whatever put inside here to insert
        cursor = self._db.cursor() #access sql
        val = (type, user,text,likes,datecreate,commented)
        #print(val)
        cursor.execute("INSERT INTO crawleddata (type,user,text,likes,dates,commented) VALUES (%s, %s,%s, %s, %s,%s)", val)
        self._db.commit() #update database
        #print("record inserted.")
        cursor.close() #close cursor everytime after use for security purposes

    def read(self,limit):
        cursor = self._db.cursor()
        cursor.execute("SELECT * FROM crawleddata LIMIT "+(str(limit))) #select all from table(comment)
        result = cursor.fetchall()
        for x in result:
           print(x)
        # for x in result:
        #     print(x)
        cursor.close()
        return result

    def search(self,keyword):
        cursor = self._db.cursor()
        sql = "SELECT * FROM crawleddata WHERE text LIKE \"%"+keyword+"%\""
        cursor.execute(sql)
        x = cursor.fetchall()
        for result in x:
            print(result) #print result here
        cursor.close()


    def truncatetable(self):
        cursor = self._db.cursor()
        cursor.execute("TRUNCATE TABLE crawleddata")  # THIS IS TO REMOVE ITEM FROM THE TABLE SAVED PREVIOUSLY
        # updating code here
        cursor.close()