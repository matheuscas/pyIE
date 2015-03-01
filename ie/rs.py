# *-* coding:utf-8 *-*
"""Module state Rio Grande do Sul"""


def start(st_reg_number):
    """Checks the number valiaty for the Rio Grande do Sul state"""

    divisor = 11

    weights = [2, 9, 8, 7, 6, 5, 4, 3, 2]

    if len(st_reg_number) > 10:
        return False

    if len(st_reg_number) < 10:
        return False

    sum_total = 0
    for i in range(len(st_reg_number)-1):
        sum_total = sum_total + int(st_reg_number[i]) * weights[i]

    rest_division = sum_total % divisor
    digit = divisor - rest_division

    if digit == 10 or digit == 11:
        digit = 0

    return digit == int(st_reg_number[len(st_reg_number)-1])
