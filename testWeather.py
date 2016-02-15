import csv
import requests

'''
	Wind chill calculation given by: http://www.capgo.com/Resources/InterestStories/WindChill/WindChill.html
	Script ran at 9:55 pm Sunday Feb 14 for fun.
'''
link = "http://api.openweathermap.org/data/2.5/group?id="
unit = "&units=metric"

multipleRecangleZone = "http://api.openweathermap.org/data/2.5/box/city?bbox="
cluster = "&cluster=yes"
units='&units=imperial'
id = "&APPID=___INSERT_YOUR_APPID_FROM_OPENWEATHER_API_HERE___"

topLeftLon = 48.299423
topLeftLat = -79.229681
bttmRightLon = 40.139488
bttmRightLat = -65.592074

fullURL = multipleRecangleZone + str(topLeftLat) + "," + str(topLeftLon) + "," + str(bttmRightLat) + "," + str(bttmRightLon) + ",10" + cluster + id
print fullURL
r = requests.get(fullURL)
weather_data = r.json()

weather_list = weather_data['list']

with open('weatherNorthEastUS.csv', 'wb') as csvfile:
	fieldnames = ['id', 'name', 'lon', 'lat', 'temp', 'temp_min', 'temp_max', 'wind_speed', 'wind_deg', 'weather_main', 'weather_description', 'wind_chill']
	writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
	writer.writeheader()

	for i in (range(0,len(weather_list))) :
		oneCity = weather_list[i]

		id = oneCity['id']
		name = oneCity['name']
		coord = oneCity['coord']
		lon = coord['lon']
		lat = coord['lat']

		main = oneCity['main']
		temp = main['temp']
		temp_min = main['temp_min']
		temp_max = main['temp_max']

		wind = oneCity['wind']
		wind_speed = wind['speed']
		wind_deg = wind['deg']

		weather = oneCity['weather'][0]
		weather_main = weather['main']
		weather_desc = weather['description']

		temp_double = float(temp)
		wind_speed_double = float(wind_speed)

		c = 0
		if wind_speed_double < 8:
			c = -0.4488 * wind_speed_double
		else:
			c = 14.81 - 2.682 * wind_speed_double + 0.055041 * wind_speed_double**2 - 0.000575 * wind_speed_double**3 + 0.000002402 * wind_speed_double**4

		wind_chill = temp_double + c * (33.3 - temp_double) / 73.3

		writer.writerow({'id':id, 'name':name, 'lon':lon, 'lat':lat, 'temp':temp, 'temp_min':temp_min, 'temp_max':temp_max, 'wind_speed':wind_speed, 'wind_deg':wind_deg, 'weather_main':weather_main, 'weather_description':weather_desc, 'wind_chill':wind_chill})


