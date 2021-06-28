#목표 기능)
#파이썬 코드를 통해 주기적으로 챗봇에게 미세먼지 정보전달

#1. 매일 특정 시점에, 파이썬 코드로 미세먼지 정보를 가져온다.
#2. 가져온 미세먼지 정보를 텔레그램 서버로 전달한다. 
#3. 텔레그램 서버가 우리 텔레그램 채팅방으로 메세지를 전달한다.

import requests

token = '1569299742:AAE03qSoC7y5N4irqMm7KmYg7w5czL8BksA'
url = f'https://api.telegram.org/bot{token}/getUpdates'

print(url)

response = requests.get(url).json()

# chat _id를 꺼내주세요.

chat_id = response['result'][0]['message']['chat']['id']

print(chat_id)

text = '안녕? 반가워!'

message_url = f'http://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
requests.get(message_url)

# 미니 과제) 로또 번호 6개를 추천해서 보내주세요
#=================================================================

#import random

#numbers = range(1, 46)

#lotto = random.sample(numbers, 6)

#==================================================================

#파파고 요청 코드

naver_client_id = 'VommRYErtbfCxhpoeaDW'
naver_client_secret = 'mEXbFiAfTO'

papago_url = 'https://openapi.naver.com/v1/papago/n2mt'

data = {
    'source': 'ko',
    'target': 'en',
    'text': '우리 광주 1반 한 학기 파이팅!',
}


headers = {
    'X-Naver-Client-Id': naver_client_id,
    'X-Naver-Client-Secret': naver_client_secret,
}

response = requests.post(papago_url, data=data, headers=headers).json()

trasnlated_text = response['message']['result']['translatedText']


text = f'{data["text"]} 문장의 번역 결과는 {trasnlated_text}입니다.'

papago_url = f'http://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'

requests.get(papago_url)

#====================================================================

# 미세먼지 코드

key = '1JPwCQgdNzAEKtE1lSxsm01P%2BrgWh6LL51sgUSnHBplnouOxUTHR%2BpTu2FzJwTMkXfXRQboUrLrJbUgWES5EHg%3D%3D'
return_type = 'json'
rows = 100
page_no = 1
sido_name = '서울'
version = '1.0'

url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?servicekey={key}&numOFRows={rows}&pageNo={page_no}&returnType={return_type}&sidoName={sido_name}&ver={version}'

response = requests.get(url).json()

sido_name = response['response']['body']['items'][0]['sidoName']
value = response['response']['body']['items'][0]['pm10Value']

text = (f'{sido_name}의 미세먼지 농도는 {value}입니다.')


dust_url = f'http://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'

requests.get(dust_url)





