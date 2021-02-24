N = int(input())
arr = list(map(int, input().split()))
Max_count = 1 #....?????? Max_count = 0 -> 1로 바꾸었더니 됐다..?
              # 아..... 수열이 하나만 주어졌을때 ㅡㅡ
count = 1 # arr[i]와 arr[i+1]의 관계를 보고 카운팅을 하는데 요구사항은 수열의 길이이므로 디폴트값은 1
for j in range(len(arr)-1):
    if arr[j] >= arr[j+1]:  # 만약 왼쪽이 오른쪽보다 크거나 같으면
        count += 1 # 추가
    else: # 아닌경우
        count = 1 # 초기화

    if Max_count <= count:
        Max_count = count

count = 1   # 반대도 검색
for j in range(len(arr)-1):
    if arr[j] <= arr[j+1]:
        count += 1
    else:
        count = 1

    if Max_count < count:
        Max_count = count

print(Max_count)

