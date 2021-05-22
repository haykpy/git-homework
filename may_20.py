import json
import os

print(os.getcwd())

with open()


class Actor:
    def __init__(self, name, surname, age, height, married, movies):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
        self.married = married
        self.movies = movies

    def present(self):
        return F"{self.name}\n{self.surname}\n{self.age}\n{self.height}\n{self.married}\n{self.movies}\n"


    def __repr__(self):
        return F"{self.name}-{self.surname} "   

    def optimal_wight(self):
        height = str(self.height).split('.')[1]
            if len(height) == 1:
                height = int(height) * 10
            else:
                height = int(height)

        return height - 10    


    def to_json(self):
        data_ = {
            'name': self.name,
            'surname': self.surname,
            'age': self.age,
            'movies': self.movies
        }

        return data_



actors = []

for item in data["items"]:
    print(F"item = {item}")
    actors.append(
        Actor(
            name = item["name"]),
            surname = item["surname"],
            age = item["age"],
            height = item["height"],
            married = item["married"],
            movies = item["movies"],
        )

print(actors[0].present())

filtered_actors = []

for actor in actors:
    if actor.age < 39:
        print(actor.present())
        print(actor.optimal_wight())
        filtered_actors.append(actor.to_json())



json_data = {"items":filtered_actors}
print(filtered_actors)


with open('filtered_json.json', 'w') as json_file:
    json.dump(json_data, json_file, indent = 4)
