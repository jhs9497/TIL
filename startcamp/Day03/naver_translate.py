import requests

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

