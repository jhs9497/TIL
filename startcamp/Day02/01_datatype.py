# 숫자
number  = 3
print(type(number))

# 문자
string = 'hello!!!'
print(type(string))

# boolean
boolean = True
print(type(boolean))

# 형변환 (datatype 변경)
string_number = '5'
number = int(string_number)
print(number + 5)

# f-string / string interpolation
name = '조현식'
print(f'안녕하세요. {name}입니다. 반갑습니다.')

# Tip. 주석 (comments)
# 이 라인은 주석입니다. 실제 실행되는 코드는 아닙니다.
'''
여러줄의 주석을 작성할 때는 따옴표 세개로 감싸줍니다.
이런식으로 여러줄을 작성할 수 있습니다. 
'''