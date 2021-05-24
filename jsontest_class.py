import json
import os
from datetime import datetime

print(os.getcwd())

class Actor(object):
    def __init__(self, name, surname, age, height, married, movies):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
        self.married = married
        self.movies = movies

    def __repr__(self):
        return F"{self.name}-{self.surname}"

    def present(self):
        return "{}\n{}\n{}\n{}\n{}\n{}".format(self.name, self.surname, self.age, self.height, self.married, self.movies)

    def optimal_weight(self):
        # 1.6  ['1', '6']
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

with open("sample_json.json", "r") as json_file:
    # print(json_file)
    data = json.load(json_file)
    print(F"data is \n{data} \n {type(data)}")

actors = []
for item in data["items"]:
    # print("item = {}".format(item))
    actors.append(Actor(item["name"], item["surname"], item["age"], item["height"], item["married"], item["movies"])
        # Actor(
        #     name=item["name"],
        #     surname=item["surname"],
        #     age=item["age"],
        #     height=item["height"],
        #     married=item["married"],
        #     movies=item["movies"]
        # )
    )

print(actors)

filtered_actors = []
for actor in actors:
    if actor.age < 39:
        print(actor.present())
        print(actor.optimal_weight())
        filtered_actors.append(actor.to_json())

# json_data = {"items":filtered_actors}
# print(filtered_actors)
# class A:
#     pass
# json_data = {
#     "month": A(),
#     "curren_time": (datetime.now())
# }

# class MyJSONEncoder(json.JSONEncoder):
#     #
#     # def __init__(self, *args, **kwargs):
#     #     super().__init__()
#
#     def default(self, o):
#         if isinstance(o, datetime):
#             return str(o)
#
#         return 5
#         # json.JSONEncoder.default(o)
# def foo(o):
#     return
#
# with open("filtered_json.json", "w") as json_file:
#     json.dump(json_data, json_file, indent=4, cls=MyJSONEncoder)

data = {
    'date': str(datetime.now())

}
with open("filtered.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

def date_parser(object):
    print(object, type(object))
    if type(object["date"]) == str:
        # 2021-05-20 [2021, 05, 20]
        obj = object["date"].split(" ")[0].split("-")
        date = datetime(year=int(obj[0]), month=int(obj[1]), day=int(obj[2]))
        object['date'] = date

    return object
a = """{
    "date": "2021-05-20 21:36:54.582854"
}"""

data_a = json.loads(a)
print(data_a, "----------")
# with open("filtered.json", "r") as json_file:
#     data = json.load(json_file, object_hook=date_parser)

# print(data, "aa")

