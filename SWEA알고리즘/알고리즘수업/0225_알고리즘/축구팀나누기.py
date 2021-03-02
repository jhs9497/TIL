import random

A = ['현철']
B = ['희철']

Defense = ['재빈', '정훈', '기석', '석빈', '용재', '환도']
Midfield = ['재훈', '상재', '병윤', '현웅', '현식', '민성']
Attack = ['신근', '지용', '아론', '덕수']

random.shuffle(Defense)
random.shuffle(Midfield)
random.shuffle(Attack)
for i in range(len(Defense)):
    if i % 2 == 0:
        A.append(Defense[i])
    B.append(Defense[i])
for i in range(len(Midfield)):
    if i % 2 == 0:
        A.append(Midfield[i])
    B.append(Midfield[i])

for i in range(len(Attack)):
    if i % 2 == 0:
        A.append(Attack[i])
    B.append(Attack[i])


print('A팀은 {} 입니다'.format(*A))
print('B팀은 {} 입니다'.format(*B))
