# *-* coding:utf-8 *-*
"""Module states Mato Grosso"""


def start(st_reg_number):
    """Checks the number valiaty for the Mato Grosso state"""
    #st_reg_number = str(st_reg_number)
    weights = [3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    digit_state_registration = st_reg_number[-1]

    if len(st_reg_number) != 11:
        return False

    sum = 0

    for i in range(0, 10):
        sum = sum + weights[i] * int(st_reg_number[i])

    if sum % 11 == 0:
        return digit_state_registration[-1] == '0'

    digit_check = 11 - sum % 11

    return str(digit_check) == digit_state_registration
