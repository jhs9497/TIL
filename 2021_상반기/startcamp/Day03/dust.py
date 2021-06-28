import requests
#from pprint import pprint <- 이쁘게 프린트해줘

#필수 요청변수
key = '1JPwCQgdNzAEKtE1lSxsm01P%2BrgWh6LL51sgUSnHBplnouOxUTHR%2BpTu2FzJwTMkXfXRQboUrLrJbUgWES5EHg%3D%3D'
return_type = 'json'
rows = 100
page_no = 1
sido_name = '서울'
version = '1.0'

url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?servicekey={key}&numOFRows={rows}&pageNo={page_no}&returnType={return_type}&sidoName={sido_name}&ver={version}'

response = requests.get(url).json()
print(response)

# '광진구의 미세먼지 농도는 pm10valu입니다.' 라는 메세지를 출력해주세요

# 내가 한 코딩


sidoname = response['items'][0]['stationName'] #<- 위에 설정한 변수값이 response = requests.get(url).json() 이라서 헷갈렸었다. 만약 
#변수값이 ABC = requests.get(url).json() 였다면 sidoname = ABC['response']['body']['items'][0]['sidoName'] 이렇게 코딩 가능
pm10Valu = response['items'][0]['pm10Value']

print(f'{sidoname}의 미세먼지 농도는 {pm10Valu}입니다.')


# 교수님 정답 풀이

sido_name = response['response']['body']['items'][0]['sidoName']
value = response['response']['body']['items'][0]['pm10Value']

print(f'{sido_name}의 미세먼지 농도는 {value}입니다.')