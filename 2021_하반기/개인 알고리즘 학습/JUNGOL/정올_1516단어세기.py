door = 'OPEN'
while door == 'OPEN':
    # 리스트 형식으로 빈 칸 기준 나눠서 인풋받기
    Sentence = list(input().split())
    # 만약 END면 그만하기
    if Sentence == ['END']:
        door = 'CLOSE'
        break
    else:
        word_list = []
        for w in Sentence:
            word_list.append(w)

    # Sentence의 각 단어를 추가한 word_list를 set화 하면서 중복제거하고
    # 다시 리스트로 만들고 sort로 정렬
    word_list = set(word_list)
    word_list = list(word_list)
    word_list.sort()
    # word_list 길이만큼 word_count 리스트 만들어줘서 개수 셀 때 활용
    word_count = [0] * len(word_list)

    for w in Sentence:
        for i in range(len(word_list)):
            # 만약 Sentence의 한 단어가 word_list의 i번째 단어와 같다면
            # word_count의 i번째에 개수 1 추가
            if w == word_list[i]:
                word_count[i] += 1

    for i in range(len(word_list)):
        print(f'{word_list[i]} : {word_count[i]}')

