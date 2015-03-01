# *-* coding:utf-8 *-*
"""Module states Paraiba"""


def start(st_reg_number):
    """Checks the number valiaty for the Paraiba state"""
    #st_reg_number = str(st_reg_number)
    weights = [9, 8, 7, 6, 5, 4, 3, 2]
    digit_state_registration = st_reg_number[-1]

    if len(st_reg_number) != 9:
        return False

    sum_total = 0

    for i in range(0, 8):
        sum_total = sum_total + weights[i] * int(st_reg_number[i])

    if sum_total % 11 == 0:
        return digit_state_registration[-1] == '0'

    digit_check = 11 - sum_total % 11

    return str(digit_check) == digit_state_registration
