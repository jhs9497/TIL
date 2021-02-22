# 간단하게 생각하자 반사고 나발이고
# 결국 x는 x축 위에서만 왔다갔다 하고
# y는 y축 위에서만 왔다갔다 한다.

w, h = map(int, input().split())
x, y = map(int, input().split())
t = int(input())

# w가 6이라고 치면 결국 x는 [0,1,2,3,4,5,6,5,4,3,2,1] 으로 움직인다
# y가 4라고 지면 y는 [0,1,2,3,4,3,2,1] 로 움직인다
# 우선 w와 h에 따라서 x, y가 움직이는 리스트를 만들어주자

w_list = []
h_list = []

# w_list 만들기
for i in range(w):
    w_list.append(i)
for j in range(w, 0, -1):
    w_list.append(j)
print(w_list)
# h_list 만들기
for i in range(h):
    h_list.append(i)
for j in range(h, 0, -1):
    h_list.append(j)
print(h_list)
# x의 인덱스 값은 초기 x값 + 움직인 횟수 t값을 w_list의 전체길이 (=2h)로 나눈 것의 나머지값을 인덱스로 한다
# y도 마찬가지

x_t = w_list[(x+t) % (2*w)]
y_t = h_list[(y+t) % (2*h)]

print(x_t, y_t)