import requests

name='hyunsik'
API_URL = f'https://api.agify.io/?name={name}'

response = requests.get(API_URL).json()
print(response)
print(type(response))

name = response['name']
age = response['age']

print(f'{name}의 나이는 {age}입니다.')