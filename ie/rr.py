# *-* coding:utf-8 *-*
"""Module state Roraima"""


def start(st_reg_number):
    """Checks the number valiaty for the Roraima state"""

    divisor = 9

    if len(st_reg_number) > 9:
        return False

    if len(st_reg_number) < 9:
        return False

    if st_reg_number[0:2] != "24":
        return False

    sum_total = 0
    peso = 1
    for i in range(len(st_reg_number)-1):
        sum_total = sum_total + int(st_reg_number[i]) * peso
        peso = peso + 1

    digit = sum_total % divisor

    return digit == int(st_reg_number[len(st_reg_number)-1])
