# *-* coding:utf-8 *-*
"""Module states Amapa"""


def start(st_reg_number):
    """Checks the number valiaty for the Alagoas state"""

    divisor = 11
    if len(st_reg_number) > 9:
        return False

    if len(st_reg_number) < 9:
        return False

    if st_reg_number[0:2] != "03":
        return False

    aux = int(st_reg_number[0:len(st_reg_number) - 1])

    if 3000000 < aux and aux < 3017001:
        control1 = 5
        control2 = 0

    if 3017000 < aux and aux < 3019023:
        control1 = 9
        control2 = 1

    if aux > 3019022:
        control1 = 0
        control2 = 0
    sum_total = 0
    peso = 9
    for i in range(len(st_reg_number)-1):
        sum_total = sum_total + int(st_reg_number[i]) * peso
        peso = peso - 1
    sum_total += control1

    rest_division = sum_total % divisor
    digit = divisor - rest_division

    if digit == 10:
        digit = 0

    if digit == 11:
        digit = control2

    return digit == int(st_reg_number[len(st_reg_number)-1])
