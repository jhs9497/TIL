import requests
from bs4 import BeautifulSoup

KOSPI_URL = 'https://finance.naver.com/sise/'

#1. 응답으로 무언가 오는데, 거기서 HTML 문서만 보여줘
response = requests.get(KOSPI_URL).text

#2. 문서(HTML)를 파이썬이 이해하기 좋게끔 구조화시켜줘
soup = BeautifulSoup(response, 'html.parser')

#3. 구조화된 문서에서 내가 원하는 정보를 가져와줘
kospi = soup.select_one('#KOSPI_now')

print(f'현재 코스피 지수는 {kospi.text}입니다')