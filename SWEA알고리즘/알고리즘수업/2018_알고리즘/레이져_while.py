for tc in range(1, int(input())+1):
    # 우선 다루기 쉽게 리스트로 바꾼다
    rough = input()
    rough_list = []
    for r in range(len(rough)):
        rough_list += [rough[r]]

    idx = 0
    count = 0
    open_iron = 0
    razer = 0
    close_iron = 0

    while idx < len(rough_list):
        if rough_list[idx] == '(' and rough_list[idx+1] == ')':
            