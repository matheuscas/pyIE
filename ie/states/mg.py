# *-* coding:utf-8 *-*
"""Module states Minas Gerais"""


def start(st_reg_number):
    """Checks the number valiaty for the Minas Gerais state"""
    #st_reg_number = str(st_reg_number)
    number_state_registration_first_digit = st_reg_number[0:3] + '0' + st_reg_number[3: len(st_reg_number)-2]
    weights_first_digit = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
    wights_second_digit = [3, 2, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    first_digit = st_reg_number[-2]
    second_digit = st_reg_number[-1]
    sum_first_digit = 0
    sum_second_digit = 0
    sum_result_digit = ''
    sum_end = 0

    if len(st_reg_number) != 13:

        return False

    for i in range(0, 12):

        sum_first_digit = weights_first_digit[i] * int(number_state_registration_first_digit[i])

        sum_result_digit = sum_result_digit + str(sum_first_digit)

    for i in range(0, len(sum_result_digit)):

        sum_end = sum_end + int(sum_result_digit[i])

    if sum_end % 10 == 0:

        check_digit_one = 0

    elif sum_end < 10:

        check_digit_one = 10 - sum_end

    elif sum_end > 10:

        check_digit_one = (10 - sum_end % 10)

    if str(check_digit_one) != first_digit:

        return False

    number_state_registration_second_digit = st_reg_number + str(check_digit_one)

    for i in range(0, 12):

        sum_second_digit = sum_second_digit + wights_second_digit[i] * int(number_state_registration_second_digit[i])

    check_second_digit = 11 - sum_second_digit % 11

    if sum_second_digit == 1 or sum_second_digit == 0:

        return second_digit == '0'

    else:
        return str(check_second_digit) == second_digit
