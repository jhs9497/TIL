def game(first, last):
    if last - first == 1:
        if arr[last] == '1':


    elif last - first == 2:
        r1 = game(first, last -1)
        r2 = last
        if arr[r1] == '1':