# *-* coding:utf-8 *-*
"""Module state Rio de Janeiro"""


def start(st_reg_number):
    """Checks the number valiaty for the Rio de Janeiro state"""
    divisor = 11

    weights = [2, 7, 6, 5, 4, 3, 2]

    if len(st_reg_number) > 8:
        return False

    if len(st_reg_number) < 8:
        return False

    sum_total = 0
    for i in range(len(st_reg_number)-1):
        sum_total = sum_total + int(st_reg_number[i]) * weights[i]

    rest_division = sum_total % divisor
    digit = divisor - rest_division

    if rest_division < 2:
        digit = 0

    return digit == int(st_reg_number[len(st_reg_number)-1])
