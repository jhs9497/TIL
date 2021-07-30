razer = list(input())

total_tree = 0
total_count = 0
open_count = 0
now = ''
for value in razer:
    if value == '(':
        open_count += 1
        now = '('

    else:
        if now == '(': # 레이저란 소리
            open_count -= 1
            total_count += open_count
            now = ')'

        elif now == ')': # 나무란 소리
            open_count -= 1
            total_tree += 1
            now = ')'


print(total_count + total_tree)