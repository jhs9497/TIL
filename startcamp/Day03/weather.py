import requests

#ex) /api/location/search/?query=london

url = 'https://www.metaweather.com/api/location/search/?query=seoul'

response = requests.get(url).json()


# [{'title': 'Seoul', 'location_type': 'City', 'woeid': 1132599, 'latt_long': '37.557121,126.977379'}]

woeid = response[0]['woeid']
print(woeid)

url2 =f'https://www.metaweather.com/api/location/{woeid}/'

response2 = requests.get(url2).json()


date = response2['consolidated_weather'][0]['applicable_date']
max = response2['consolidated_weather'][0]['max_temp']
min = response2['consolidated_weather'][0]['min_temp']

print(f'서울의 {date} 최고기온은 {max}도 이고 최저기온은 {min}도 입니다.')