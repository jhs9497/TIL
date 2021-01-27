def dec_to_bin(n):
    '''
    2/5 ...1
    2/2 ...0
    1
    '''

    # 재귀의 핵심은 반복되는 부분이 무엇인지
    # 그리고 그 반복되는 부분이 언제 끝나는지 파악하는 게 중요!
    # base case를 찾아라!

    # 지금 반복되는 부분은 ? 2로 나누는 '행위'
    # 종료되는 시점은 ? 마지막으로 나눴을 때 몫이 2 미만일때
    # 원하는 최종 결과값은? => 마지막 몫 + 이전 나눗셈들의 나머지들

    if n < 2:
        return str(n)
    
    return dec_to_bin(n // 2) + str(n % 2)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(dec_to_bin(10))
    # => '1010'
    print(dec_to_bin(5))
    # => '101'
    print(dec_to_bin(50))
    # => '110010'