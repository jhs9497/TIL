T = int(input())
 
for tc in range(1, T+1):
 
    tc_num, N = map(str, input().split())
    N = int(N)
     
    print("#{}".format(tc))
 
    # print(tc_num, N, type(N))
 
    str_nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    str_dict = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
    num_cnt = [0]*len(str_nums)
 
    input_data = list(map(str, input().split()))
 
    for i in range(N):
        if input_data[i] in str_dict: # ONE
            num_cnt[str_dict[input_data[i]]] += 1
 
    for i in range(len(num_cnt)):
        print((str_nums[i]+' ') * num_cnt[i])