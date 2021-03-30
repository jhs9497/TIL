N,K=map(int,input().split())
R=0
for i in range(1,N+1):
    R=(R+K)%i
print(R+1)