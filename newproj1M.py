import sqlite3

class newproj1M:
    def __init__(self):
        self.con = sqlite3.connect("newproj1Db.db")

        self.cur = self.con.cursor()
        self.cur.execute(
        'create table if not exists USERS (userName , Password)'
        )
        self.cur.execute("INSERT INTO USERS(userName,Password) VALUES(?,?)" , ('mmad@gmail.com' , '1qaz!QAZ'))
        self.con.commit()
    
    def checkPassword(self , user , password):
      res = self.cur.execute("SELECT * FROM USERS WHERE userName=? AND password=?" ,  (user,password))
      dat = res.fetchone()
      if dat != None:
        return True
      else:
        return False
      
