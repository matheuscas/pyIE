# *-* coding:utf-8 *-*
"""Module states Pernanbuco"""


def start(st_reg_number):
    """Checks the number valiaty for the Pernanbuco state"""
    divisor = 11

    if len(st_reg_number) > 9:
        return False

    if len(st_reg_number) < 9:
        return False

    sum_total = 0
    peso = 8
    for i in range(len(st_reg_number)-2):
        sum_total = sum_total + int(st_reg_number[i]) * peso
        peso = peso - 1

        rest_division = sum_total % divisor
        digit_first = divisor - rest_division

    if rest_division < 2:
        digit_first = 0

    if rest_division > 1:
        digit_first = 11 - rest_division

    num = 0
    peso = 9
    mult = 10000000
    for i in range(len(st_reg_number)-2):
        num = num + int(st_reg_number[i]) * mult
        mult = mult // 10

    num = num + digit_first

    new_st = str(num)
    sum_total = 0
    peso = 9
    for i in range(len(new_st)-1):
        sum_total = sum_total + int(new_st[i]) * peso
        peso = peso - 1

    rest_division = sum_total % divisor

    if rest_division < 2:
        digit_secund = 0

    if rest_division > 1:
        digit_secund = divisor - rest_division

    if digit_secund == int(st_reg_number[len(st_reg_number)-1]) and digit_first == int(st_reg_number[len(st_reg_number)-2]):
        return True
    else:
        return False
