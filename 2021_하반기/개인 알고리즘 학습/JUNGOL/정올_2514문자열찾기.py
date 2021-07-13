S = input()
KOI = 0
IOI = 0
for i in range(len(S)-2):
    part = S[i] + S[i+1] + S[i+2]
    if part == 'KOI':
        KOI += 1
    elif part == 'IOI':
        IOI += 1

print(KOI)
print(IOI)
