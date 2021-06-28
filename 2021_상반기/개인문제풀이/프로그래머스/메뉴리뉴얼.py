from itertools import combinations

# 오답 2개 / 시간초과 3개

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

menu = set() # 조합 돌릴 리스트 만들기

for i in range(len(orders)):
    for j in range(len(orders[i])):
        menu.add(orders[i][j])

course_list = []
for i in range(course[0], course[-1]+1): # course 첫번쨰와 마지막번째 숫자 내에서
    more_count = 0 # 마지막 최종코스에 등록하기 전 체크
    course_sub = [] # 코스 후보군
    for j in combinations(menu, i): # 조합으로 뽑아내고 (2~4가지)
        course = list(j)
        course.sort()
        course = ''.join(course) # 후보가 될 친구들

        count = 0
        for a in range(len(orders)): # "ABCFG" 요걸보면서
            small_count = 0
            for b in range(len(orders[a])):
                if orders[a][b] in course: # A, B, C, F, G 하나씩 돌면서 만약 course안에 있으면
                    small_count += 1 # +1

            if small_count == len(course): # 마지막 for문 돌고 쌓인 samll_count가 course길이랑 같으면 완전히 속했다는 뜻이니
                count += 1 # count + 1

        if count >= 2: # count가 2 이상이면 최종후보에 오를만 하니
            course_sub.append((course, count)) # 최종후보에 count와 함꼐 추가
            if more_count < count: # 가장 큰 count값만 남게 만들기
                more_count = count

    for S in range(len(course_sub)): # 최종 후보 돌면서
        if course_sub[S][1] == more_count: # 가장 큰 count 값이랑 같은 후보친구만
            course_list.append(course_sub[S][0]) # 최종코스리스트에 추가

course_list.sort()

print(course_list)

