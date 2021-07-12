A, N, B = input().split()

ten_number = 0

for i in range(len(N)-1, -1, -1):
    
    ten_number += int(N[i])*int(A)**(len(N)-1-i)

print(ord('A'))

print(ten_number)