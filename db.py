import mysql.connector as c
mydb=c.connect(
    host="localhost",
    user="root",
    password="cvr123",
    database="cvr"
)

mycursor=mydb.cursor()

#mycursor.execute("CREATE TABLE movie (moviename VARCHAR(255), collections int, year int, hero VARCHAR(100))")

#mycursor.execute("INSERT INTO movie(moviename,collections,year,hero) VALUES('hi',2300,2025,'raj')")
#mycursor.execute("INSERT INTO movie (moviename, collections, year, hero) VALUES ('blockbuster', 15000, 2023, 'arjun')")
#mycursor.execute("INSERT INTO movie (moviename, collections, year, hero) VALUES ('action king', 5000, 2022, 'vikram')")


mycursor.execute("select *from movie where year=2023")
st=mycursor.fetchall();
for i in st:
    print(i)



mydb.commit()



























#name=input("enter your name")
#id=input("enter your id")

#mycursor.execute("select *from prateek")
#st=mycursor.fetchall();
#for i in st:
 #   print(i)


#mycursor.execute("create table prateek(sid int,sname varchar(20))")
#mycursor.execute("INSERT INTO prateek(sid,sname) VALUES(123, 'raj')")
#mycursor.execute("delete from prateek where sid=123")

#print("Record inserted successfully")

#mydb.commit()