# *-* coding:utf-8 *-*
"""Module state Rio Grande do Norte"""


def start(st_reg_number):
    """Checks the number valiaty for the Rio Grande do Norte state"""

    divisor = 11

    if len(st_reg_number) > 10:
        return False

    if len(st_reg_number) < 9:
        return False

    if st_reg_number[0:2] != "20":
        return False

    sum_total = 0
    peso = len(st_reg_number)
    for i in range(len(st_reg_number)-1):
        sum_total = sum_total + int(st_reg_number[i]) * peso
        peso = peso - 1

    mult = sum_total * 10
    digit = mult % divisor

    if digit == 10:
        digit = 0

    return digit == int(st_reg_number[len(st_reg_number)-1])
