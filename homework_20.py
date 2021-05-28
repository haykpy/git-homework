import datetime

def weather(city):
	print(F"Weather is 32C in {city}")

def my_decorator(func):
	def decor(time):
		current_date = datetime.datetime.now()
		print(F"Current date/time is {current_date}")
		func(time)
	return decor


@my_decorator
def weather(city):
	print("Weather is 32C in Yerevan")
weather("Yerevan")	
