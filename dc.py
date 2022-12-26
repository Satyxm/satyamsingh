# This program is all about dictionary comprehension.

weather = {'New york' : 'foggy', 'Chicago' : 'sunny', 'Brooklyn' : 'rainy', 'Boston' : 'sunny'}
sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}
print(sunny_weather)
