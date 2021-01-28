

test_case = int(input())

for i in range(1, test_case+1):

    number = input()



    month_A_str = '01', '03', '05', '07', '08', '10', '12'
    month_B_str = '04', '06', '09', '11'
    month_C_str = '02'


    #date_A_str = str(list(range(1, 32)))
    #date_B_str = str(list(range(1, 31)))
    #date_C_str = str(list(range(1, 29)))


    date_A_str = '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'
    date_B_str = '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30' 
    date_C_str = '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28'




    original = ''

    for j in str(number):
        original += j
        
    
    if original[4:6] in month_A_str and original[6:8] in date_A_str:

        result = original[0:4] + '/' + original[4:6] + '/' + original[6:]
        print(f'#{i}', result)

    elif original[4:6] in month_B_str and original[6:8] in date_B_str:
        result = original[0:4] + '/' + original[4:6] + '/' + original[6:]
        print(f'#{i}', result)

    elif original[4:6] in month_C_str and original[6:8] in date_C_str:
        result = original[0:4] + '/' + original[4:6] + '/' + original[6:]
        print(f'#{i}', result)

    else:
        print(f'#{i} -1')




    