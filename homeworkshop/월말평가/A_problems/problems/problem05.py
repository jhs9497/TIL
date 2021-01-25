def dec_to_bin(n):
    number = '1'
    while n // 2 > 1:
        
        if n % 2 == 1:
            number += '0'
        else:
            number += '1'

        n = n / 2
        
    return number


# % : 나머지 반환
# // : 몫 반환


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(dec_to_bin(10))
    # => '1010'
    print(dec_to_bin(5))
    # => '101'
    print(dec_to_bin(50))
    # => '110010'