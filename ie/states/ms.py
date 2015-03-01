# *-* coding:utf-8 *-*
"""Module states Mato Grosso do Sul"""


def start(st_reg_number):
    """Checks the number valiaty for the Mato Grosso do Sul state"""

    divisor = 11

    if len(st_reg_number) > 9:
        return False

    if len(st_reg_number) < 9:
        return False

    if st_reg_number[0:2] != "28":
        return False

    sum_total = 0
    peso = 9
    for i in range(len(st_reg_number)-1):
        sum_total = sum_total + int(st_reg_number[i]) * peso
        peso = peso - 1

    rest_division = sum_total % divisor

    if rest_division == 0:
        digit = 0

    else:
        digit = divisor - rest_division
        if digit > 9:
            digit = 0

    return digit == int(st_reg_number[len(st_reg_number)-1])
