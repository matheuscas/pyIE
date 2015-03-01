# *-* coding:utf-8 *-*
"""Module state Rondônia"""


def start(st_reg_number):
    """Checks the number valiaty for the Rondônia state"""

    divisor = 11

    weight = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    if len(st_reg_number) != 9 and len(st_reg_number) != 14:
        return False

    if len(st_reg_number) == 9:
        sum_total = 0
        peso = 6
        for i in range(3, len(st_reg_number)-1):
            sum_total = sum_total + int(st_reg_number[i]) * peso
            peso = peso - 1

        rest_division = sum_total % divisor
        digit = divisor - rest_division

        if digit == 10:
            digit = 0

        if digit == 11:
            digit = 1

        return digit == int(st_reg_number[len(st_reg_number)-1])

    else:
        sum_total = 0
        for i in range(len(st_reg_number)-1):
            sum_total = sum_total + int(st_reg_number[i]) * weight[i]

        rest_division = sum_total % divisor
        digit = divisor - rest_division

        if digit == 10:
            digit = 0

        if digit == 11:
            digit = 1

        return digit == int(st_reg_number[len(st_reg_number)-1])
