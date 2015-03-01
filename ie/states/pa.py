# *-* coding:utf-8 *-*
"""Module states Para"""


def start(st_reg_number):
    """Checks the number valiaty for the Para state"""
    divisor = 11

    if len(st_reg_number) > 9:
        return False

    if len(st_reg_number) < 9:
        return False

    if st_reg_number[0:2] != "15":
        return False

    sum_total = 0
    peso = 9
    for i in range(len(st_reg_number)-1):
        sum_total = sum_total + int(st_reg_number[i]) * peso
        peso = peso - 1

    rest_division = sum_total % divisor
    digit = divisor - rest_division

    if rest_division < 2:
        digit = 0

    if rest_division > 1:
        digit = 11 - rest_division

    return digit == int(st_reg_number[len(st_reg_number)-1])
