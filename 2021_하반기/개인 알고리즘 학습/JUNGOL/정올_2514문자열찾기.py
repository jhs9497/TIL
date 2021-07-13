S = input()
KOI = 0
IOI = 0
# 끝에서 3번째 문자까지 i로 지정하고 거기서 2칸 더 가도록 범위 설정
for i in range(len(S)-2):
    # i기준 i+1, i+2 번째 문자까지 3 문자를 얻어내기
    part = S[i] + S[i+1] + S[i+2]
    # 일치여부 확인 후 카운팅
    if part == 'KOI':
        KOI += 1
    elif part == 'IOI':
        IOI += 1

print(KOI)
print(IOI)
