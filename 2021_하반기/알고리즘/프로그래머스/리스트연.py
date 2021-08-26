A = [1,2,3,4,5,6]
now_idx = 2
n = len(A)

B = 19


down_idx = now_idx - B
if down_idx >= 0:
    now_idx = down_idx

else:
    now_idx = n - (abs(down_idx) % n)
#
#
# up_idx = now_idx + B
# if up_idx < n:
#     now_idx = up_idx
# else:
#     now_idx = up_idx % n

print(now_idx)
