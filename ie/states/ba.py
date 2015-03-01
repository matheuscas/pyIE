# *-* coding:utf-8 *-*
"""Module states Bahia"""


def start(st_reg_number):
    """Checks the number valiaty for the Bahia state"""

    weights_second_digit = range(len(st_reg_number)-1, 1, -1)
    weights_first_digit = range(len(st_reg_number), 1, -1)
    second_digits = st_reg_number[-1:]
    number_state_registration = st_reg_number[0:len(st_reg_number) - 2]
    digits_state_registration = st_reg_number[-2:]
    sum_second_digit = 0
    sum_first_digit = 0

    if len(st_reg_number) != 8 and len(st_reg_number) != 9:
        return False

    if st_reg_number[-8] in ['0', '1', '2', '3', '4', '5', '8']:

        for i in weights_second_digit:

            sum_second_digit = sum_second_digit + i*int(st_reg_number[-i-1])

        second_digits_check = 10 - (sum_second_digit % 10)

        if sum_second_digit % 10 == 0 or sum_second_digit % 11 == 1:

            second_digits_check = '0'

        if str(second_digits_check) != second_digits:

            return False

        digit_two = number_state_registration + str(second_digits_check)

        for i in weights_first_digit:

            sum_first_digit = sum_first_digit + i*int(digit_two[-i+1])

        first_digits_check = 10 - (sum_first_digit % 10)

        if sum_first_digit % 10 == 0 or sum_first_digit % 10 == 1:
            first_digits_check = '0'

        digits_calculated = str(first_digits_check) + str(second_digits_check)

        return digits_calculated == digits_state_registration

    elif st_reg_number[-8] in ['6', '7', '9']:

        for i in weights_second_digit:

            sum_second_digit = sum_second_digit + i*int(st_reg_number[-i-1])

        second_digits_check = 11 - (sum_second_digit % 11)

        if sum_second_digit % 11 == 0 or sum_second_digit % 11 == 1:
            second_digits_check = '0'

        if str(second_digits_check) != second_digits:
            return False

        digit_two = number_state_registration + str(second_digits_check)

        for i in weights_first_digit:

            sum_first_digit = sum_first_digit + i*int(digit_two[-i+1])

        first_digits_check = 11 - (sum_first_digit % 11)

        if sum_first_digit % 11 == 0 or sum_first_digit % 11 == 1:
            first_digits_check = '0'
        digits_calculated = str(first_digits_check) + str(second_digits_check)
        return digits_calculated == digits_state_registration
