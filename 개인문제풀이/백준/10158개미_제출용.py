w, h = map(int, input().split())
x, y = map(int, input().split())
t = int(input())

w_list = []
h_list = []

for i in range(w):
    w_list.append(i)
for j in range(w, 0, -1):
    w_list.append(j)

for i in range(h):
    h_list.append(i)
for j in range(h, 0, -1):
    h_list.append(j)

x_t = w_list[(x+t) % (2*w)]
y_t = h_list[(y+t) % (2*h)]

print(x_t, y_t)