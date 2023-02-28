def degree_2_in_range(n, counter):
    list_final = []
    for i in range(n, counter + 1):
        if not list_final:
            list_final.append(i)
        else:
            list_final.append(i ** 2)
    return list_final
def multiplication_and_search_palindrome(number1, number2):
    multiplier1 = 0
    multiplier2 = 0
    temp_palindrome = 0

    for i in range(number1, number2):
        temp_multiplier1 = i
        for item in range(i, number2):
            temp_multiplier2 = item
            item *= i
            palindrome = str(item)

            if palindrome == palindrome[::-1] and int(temp_palindrome) <= int(palindrome):
                temp_palindrome = int(palindrome)
                multiplier1 = temp_multiplier1
                multiplier2 = temp_multiplier2

    printing_palindrome_and_multiplication_result(temp_palindrome, multiplier1, multiplier2)


def printing_palindrome_and_multiplication_result(palindrome, multiplier1, multiplier2):
    print(f"palindrome is: {palindrome}, Multiplication of {multiplier1} * {multiplier2}")


multiplication_and_search_palindrome(1000, 10000)

    elif seq == degree_3_in_range(base_number, number_operation):
        return degree_3_in_range(base_number, number_operation + 1)[-1]

    else:
        return -1


print(f"Next number of sequence 1,8,27,64,125 is {next_number('1,8,27,64,125')}")

print(f"Next number of sequence 1,4,9,16,25 is {next_number('1,4,9,16,25')}")