# *-* coding:utf-8 *-*
"""Module state Tocantins"""


def start(st_reg_number):
    """Checks the number valiaty for the Tocantins state"""
    divisor = 11

    if len(st_reg_number) > 11:
        return False

    if len(st_reg_number) < 11:
        return False

    if st_reg_number[2:4] not in ['01', '02', '03', '99']:
        return False

    sum_total = 0
    peso = 9
    for i in range(len(st_reg_number)-1):
        if i != 2 and i != 3:
            sum_total = sum_total + int(st_reg_number[i]) * peso
            peso = peso - 1

    rest_division = sum_total % divisor
    digit = divisor - rest_division

    if rest_division < 2:
        digit = 0

    return digit == int(st_reg_number[len(st_reg_number)-1])
