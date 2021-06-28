a=[1,2,3,4,5,6,7,8,9,10]
x = 3
cnt = 0
while x > 0:
    for i in range(len(a)-1):
        if a[i+x-3]+a[i+x-2]+a[i+x-1] < a[i+x-2]+a[i+x-1]+a[i+x]:
            a[i+x-3] = a[i+x-2]
            x -= 1
            cnt += a[i+x-2]
print(cnt)