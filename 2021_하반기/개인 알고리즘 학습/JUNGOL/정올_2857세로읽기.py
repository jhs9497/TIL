word_list = []
# 입력받은 인풋값의 각 문자길이 중 가장 긴 길이 구하기
max_length = 0
for _ in range(5):
    input_list = list(input())
    word_list.append(input_list)
    if max_length < len(input_list):
        max_length = len(input_list)

for i in range(5):
    # 문자열 중 가장 긴 길이에서 각 문자열들의 길이를 뺴고
    count = max_length - len(word_list[i])
    # 만약 그 길이가 0보다 크면 현재 문자열이 짧다는 뜻이므로
    if count > 0:
        while count > 0:
            # 그 카운트 만큼 뒤에 '' 빈 값 추가
            word_list[i].append('')
            count -= 1

answer = ''

# for문을 세로로 돌리면서
for i in range(len(word_list[0])):
    for j in range(5):
        # 빈 값이면 패스하고
        if word_list[j][i] == '':
            pass
        else:
            # 아니면 정답에 추가하여 출력
            answer += str(word_list[j][i])

print(answer)
