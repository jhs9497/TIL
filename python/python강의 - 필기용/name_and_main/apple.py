def func():

    print(__name__)

if __name__ == '__main__':
    # 현재 파일이 직접 실행되었는지
    # 판별하기 위한 조건문
    # ex) python apple.py

    # 간접 실행 ?
    # == 다른 파일에서 불러와져서 실행
    func()  # __main__ 출력

