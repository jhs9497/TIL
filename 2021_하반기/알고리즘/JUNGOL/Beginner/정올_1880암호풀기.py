key = input()
password = input()

# 우선 abcdefg~~~z 까지 기준이 될 문자열 만들고
alpha = ''
for j in range(97, 123):
    alpha += chr(j)

answer = ''
for a in range(len(password)):
    # 빈 칸이면 그냥 빈 칸 추가하고
    if password[a] == ' ':
        answer += ' '
    else:
        # 빈 칸이 아닌 경우에 만약 대문자면
        if password[a].isupper():
            for b in range(len(alpha)):
                # 현재 password 알파벳 값의 소문자가 위에 만든 알파벳 (alpha)와 같은 경우의 "alpha의 b 인덱스를"
                if password[a].lower() == alpha[b]:
                    # key문자열의 위에서 alpha를 통해 구한 "b" 인덱스를 넣고 대문자로 변환시켜 answer에 더해준다
                    answer += key[b].upper()
        else:
            # 소문자일 땐 위 과정에서 소문자화 & 대문자화하는 과정만 빼면 됨
            for c in range(len(alpha)):
                if password[a] == alpha[c]:
                    answer += key[c]

print(answer)
