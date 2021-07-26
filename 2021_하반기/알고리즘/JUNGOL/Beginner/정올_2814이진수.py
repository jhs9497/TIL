# 리스트로 인풋 받고 why? 거꾸로 뒤집으려고
N = list(input())
# 리버스
N.reverse()

# answer에 더해나가준다
answer = 0

for i in range(len(N)):
    # 만약 i번째 값이 '1'이면
    if N[i] == '1':
        # answer에 2의i승 만큼 더해주면 됨!
        answer += 2**(i)

print(answer)


