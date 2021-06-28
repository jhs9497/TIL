'''
애너그램

애너그램(anagram)은 단어나 문장을 구성하고 있는 문자의 순서를 바꾸어 다른 단어나 문장을 만드는 놀이입니다.
두 문자열이 공백으로 구분되어 입력된다고 했을 때, 서로 애너그램인지 판별하는 함수를 작성하시오.
입력 문자는 모두 소문자로 빈칸 없이 제공됩니다.

---
[입력 예시]
ohlamesaint themonalisa

[출력 예시]
True
'''

def check_anagram(text1, text2):
    pass


if __name__ == '__main__': 
    print(check_anagram('ohlamesaint', 'themonalisa')) # True
    print(check_anagram('apple', 'eppla'))             # True
    print(check_anagram('banana', 'babana'))           # False