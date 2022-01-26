import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root" , passwd="1234", database ="mov_data")

mycursor =mydb.cursor()


mycursor.execute("CREATE TABLE movie(Name VARCHAR(30),Actor VARCHAR(30),Actress VARCHAR(30),Director VARCHAR(30),Year_of_release INT NOT NULL,PRIMARY KEY(Name))")
sql = "INSERT INTO movie (Name, Actor, Actress,Director,Year_of_release) VALUES (%s, %s, %s, %s, %s)"
val = [
  ('October Sky','Jake Gyllenhaal','Laura Dern','Joe Johnston',1999),
  ('INTERSTELLAR','Matthew McConaughey','Anne Hathaway','Christopher Nolan',2014),
  ('Serenity','Matthew McConaughey','Anne Hathaway','Steven Knight',2019),
  ('Spider-Man','Tobey Maguire','Kirsten Dunst','Sam Raimi',2002),
  ('The Wedding Planner','Matthew McConaughey','Jennifer Lopez','Adam Shankman',2001),
  ]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "Contents inserted.")
mycursor.execute(" SELECT * FROM movie")
for i in mycursor:
    print(i)

#print(mycursor.fetchall())

mydb.close()
