# Create databse if none exists

import mysql.connector as conn

def connectDB():
    db = conn.connect(host='localhost', user='root', passwd='')
        cursor = db.cursor()
            return db, cursor

def createDB(db, cursor):
    # create a new database
    sql = '''
        DROP DATABASE IF EXISTS KRMA_Radio;
        CREATE DATABASE KRMA_Radio;
        '''
            cursor.execute(sql, multi=True)
                db.commit

def createEntity(db, cursor):
    # use the new database
    sql = 'USE exampledb'
        cursor.execute(sql)
            sql = '''
                DROP TABLE IF EXISTS person;
                CREATE TABLE person
                (personid int not null auto_increment,
                firstname varchar(20) not null,
                lastname varchar(30) not null,
                primary key(personid))
                '''
                    cursor.execute(sql, multi=True)
                        db.commit

#main program
if __name__ == "__main__":
    
    # exception handling routine   
    try:
        db,cursor = connectDB()
        createDB(db, cursor)
        createEntity(db, cursor)
        #close the connection
        cursor.close()
    except:
        pass
