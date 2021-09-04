import random
import numpy as np

x11 = np.zeros(16)
x12 = np.zeros(16)
x13 = np.zeros(16)
x14 = np.zeros(16)
x15 = np.zeros(16)
x16 = np.zeros(16)

#6개 제품을 입고 시킬 거
#랜덤 수 던지기 => set으로 만들어서 중복이 안되게 한다?..
while sum(x11) < 30 and sum(x12) <50 and sum(x13) <20 :
    b = random.randrange(16)
    x11[b] += 1
while sum(x12) < 50 :
    b= random.randrange(16)
    if x11[b]==0 and x13[b] ==0 :
        x12[b] +=1
while sum(x13) < 100 :
    b= random.randrange(16)
    if x12[b] == 0 and x11[b]==0 :
        x13[b] += 1

print(x11)
print(x12)
print(x13)