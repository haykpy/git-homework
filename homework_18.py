import requests
import json



with open("url.json", "r") as json_file:
	data = json.load(json_file)

print(data["python"])
print(data["panther"])
print(data["nature"])

try:
	pic1 = requests.get(data["python"])

	with open("python.jpeg", "wb") as pic:
		pic.write(pic1.content)


	pic2 = requests.get(data["panther"])

	with open("panther.jpeg", "wb") as pic:
		pic.write(pic2.content)


	pic3 = requests.get(data["nature"])

	with open("nature.jpeg", "wb") as pic:
		pic.write(pic3.content)

except ConnectionError:
	print("Could not download file.")
