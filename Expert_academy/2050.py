test_case = str(input()).upper()


alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

alph_dict = {}


for i in range(len(alph)):
    
    alph_dict[alph[i]] = i+1



for char in test_case:
    result = ''
    for i in alph_dict:
        if char == i:
            result += str(alph_dict[char])
            


    print(result, end=' ')

