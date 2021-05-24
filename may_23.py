import requests
import pprint
import json

response = requests.get('https://xkcd.com/353/')
# print(F"The URL of the request{response.url}")
# print(F"Tis is the text attribute:\n\n {response.text}")
# print(F"Tis is the content attribute:\n\n {response.content}")
# print(response.request.__dict__)
# print(type(response))
# print(response)


response_2 = requests.get('https://xkcd.com/353/jdhdkhak')

# print(response.status_code, "response")
# print(response_2.status_code, "response_2")

# print(response.reason, "response")
# print(response_2.reason, "response_2")


# pprint.pprint(dir(response))


response = requests.get("https://imgs.xkcd.com/comics/python.png")
response_2 = requests.get("http://www.httpbin.org/image/jpeg")


# with open("photo1.png", "wb") as file:
#     file.write(response.content)



# with open("photo2.jpeg", "wb") as file:
#     file.write(response_2.content)


# ralf = requests.get("https://upload.wikimedia.org/wikipedia/ru/1/18/Ralph2poster.jpeg")    

# with open("ralf_photo.jpeg", "wb") as pic:
#     pic.write(ralf.content)


# google_r = requests.get("https://www.google.com/search?client=opera&q=python")
# print(google_r.text)

  
# g_params = {"q": "python"}   
# google_r = requests.get("https://www.google.com/search", params = g_params)
# print(google_r.text)
# print(google_r.url)


parameters = {"name": "python", "school": "basic_it"}
response = requests.get("https://httpbin.org/get", params = parameters)
print(response.text)
print(response.url)


r = response.json()
print(r)
print(type(r))
print(r["args"])
print(r["args"]["name"])


# POST method

dict_ = {
        "name": "Scarlett",
        "surname": "Johansson",
        "age": 35,
        "height": 1.6,
        "married": False,
        "movies": ["Black Widow", "Lucy", "The Avengers", "The Other Boleyn Girl"]
    }

# response = requests.post("https://httpbin.org/post", json = dict_)
# print(response)
# print(response.text)
# print(response.json())


data = json.dumps(dict_)
print(data, type(data))
response = requests.post("https://httpbin.org/post", data = data)
print(response)
print(response.text)




