import sqlite3
import os
import json

database = os.path.join(os.getcwd(), "film.db")
conn = sqlite3.connect(database)
curs = conn.cursor()

#1
with conn:
	curs.execute("SELECT title FROM film where title like 'B%'")

result = curs.fetchall()
print(result)



#2
with conn:
	curs.execute("SELECT title, MAX(length) FROM film ")

result_1 = curs.fetchall()
print(result_1)



#3
with conn:
	curs.execute("SELECT * FROM film")

result_2 = curs.fetchall()


with open('data.json', 'w') as jsonfile:
    json.dump(result_2, jsonfile)




#extra
with conn:
	curs.execute("SELECT * FROM film WHERE release_year > 2010 and rate BETWEEN '3' and '5'")

result_3 = curs.fetchall()
print(result_3)

for film in result_3:
	print(film)

film_query = """ CREATE TABLE IF NOT EXISTS filtered_film (
                                        film_id integer PRIMARY KEY,
                                        title text NOT NULL,
                                        description, 
                                        release_year, 
                                        rate, 
                                        length, 
                                        special_features
                                    ); """

curs.execute(film_query)
conn.commit()


def insert_function_film(value):
  insert_query = """INSERT INTO filtered_film(film_id, title, description, release_year, rate, length, special_features)
                      VALUES(?,?,?,?,?,?,?);
                      """
  curs.execute(insert_query, value)
  conn.commit()

insert_function_film(film)  
