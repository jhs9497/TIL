def solution(s):
    number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = ''
    now = ''
    for idx in range(len(s)):
        if s[idx].isdigit():
            answer += s[idx]
        else:
            now += s[idx]

        for i in range(len(number)):
            if now == number[i]:
                answer += str(i)
                now = ''
                break

    answer = int(answer)

    return answer