def check(msg, idx, dict):
    for i in range(len(msg), idx, -1):
        if msg[idx:i] in dict:
            break
    dict.append(msg[idx:i+1])
    return i, dict

def solution(msg):
    dict = ['','A','B','C','D', 'E', 'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    answer = []
    idx = 0
    while len(msg) != idx:
        i, dict = check(msg, idx, dict)
        answer.append(dict.index(msg[idx:i]))
        idx = i

    return answer

solution('KAKAO')