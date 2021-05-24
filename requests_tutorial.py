import requests
import pprint
import json

# response = requests.get('https://xkcd.com/353/')
# print(response.request.__dict__)
# print(type(response), "is the type of response")
# response_2 = requests.get('https://xkcd.com/353dsadsadsadsadsasadsa/')

# print(response.status_code, response.reason, "response")
# print(response_2.status_code, response_2.reason, "response_2")
# the attributes of the response object
# pprint.pprint(dir(response))

# print(help(response))

# the status_code attribute returns request's status 
# print(F"the status code of request is {response.status_code}")
# the url attribute returns the requested url
# print(F"the URL of the request is {response.url}")

# the text attribute returns the page as text
# print(F"this is the text attribute:\n\n{response.text}")
# print(F"this is the content attribute:\n\n{response.content}")

# lets try to download an image, and find out another method of open: wb

# response = requests.get('https://imgs.xkcd.com/comics/python.png')
# response_2 = requests.get('http://www.httpbin.org/image/jpeg')
# # # print(response.text)
# # # print(response.content)
#
# with open("new2_photo.png", 'wb') as file:
#     file.write(response.content)
#
# with open("new3_photo.jpeg", 'wb') as file:
#     file.write(response_2.content)

# how to send parameters to a url
# g_params = {"q": "python"}
# google_r = requests.get("https://www.google.com/search", params=g_params)
# print(google_r.url)
# print(google_r.text)
# print()

parameters = {"name": "python", "school": "basic IT"}
#
# response = requests.get('https://httpbin.org/get', params=parameters)
# # response = requests.get('https://httpbin.org/get?name=python&school=basic+IT')
# print(response.url)
# print(response.text)
#
#
# r = response.json()
# print(r)
# print(type(r))
# print(r['args'])
# print(r['args']["name"])


# let's test POST method with https://httpbin.org
dict_ = {
        "name": "Scarlett",
        "surname": "Johansson",
        "age": 35,
        "height": 1.6,
        "married": False,
        "movies": ["Black Widow", "Lucy", "The Avengers", "The Other Boleyn Girl"]
    }
response = requests.post('https://httpbin.org/post', json=dict_)  # as a forms

print(response)
print(response.text)

print(response.json())

#
# # now let's send json object
data = json.dumps(dict_)
print(data, type(data))
response = requests.post('https://httpbin.org/post', data=data)  # as a forms

print(response)
print(response.text)