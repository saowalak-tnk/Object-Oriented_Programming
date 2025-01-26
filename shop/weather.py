import requests 
apikey = "b1057e841e66befa4a8f2d4c7b988a48"
city = "bangkok" 
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}'
url_json = f'https://api.openweathermap.org/data/2.5/weather?q=Seoul&appid=b1057e841e66befa4a8f2d4c7b988a48'
result = requests.get(url).json()
#print(result)
city = result['name']
country = result['sys']['country']
weather = result['weather'][0]['main']
description = result['weather'][0]['description']
temp = result['main']['temp'] -273.15

print(f'เมือง {city} ประเทศ {country} ')
print(f'สภาพอากาศ {weather} {description}')
print(f'อุณหภูมิ {temp:.2f} องศาเซลเซียส')