key = input()
password = input()

alpha = ''
for j in range(97, 123):
    alpha += chr(j)

answer = ''
for a in range(len(password)):
    if password[a] == ' ':
        answer += ' '
    else:
        if password[a].isupper():
            for b in range(len(alpha)):
                if password[a].lower() == alpha[b]:
                    answer += key[b].upper()
        else:
            for c in range(len(alpha)):
                if password[a] == alpha[c]:
                    answer += key[c]

print(answer)
