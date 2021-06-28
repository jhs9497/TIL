# 딕셔너리 선언
my_home = {
    'location': 'seoul',
    'area-code': '02'
}

# 딕셔너리 원소 접근

location = my_home['location']
area_code = my_home['area-code']
print(location)
print(area_code)
# 에러 발생하는 경우
# print(my_home['population'])

my_home.get('location')
my_home.get('area-code')
print(location)
print(area_code)
print(my_home.get('population'))

# 딕셔너리 원소 변경
my_home['location']='gwangju'
print(my_home)

my_home['area-code']= '062'
print(my_home)