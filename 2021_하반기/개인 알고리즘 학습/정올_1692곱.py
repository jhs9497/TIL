first_number = int(input())
second_number = int(input())
second_number = str(second_number)

number_3 = first_number * int(second_number[2])
number_4 = first_number * int(second_number[1])
number_5 = first_number * int(second_number[0])

number_6 = first_number * int(second_number)

print(number_3, number_4, number_5, number_6, sep='\n')