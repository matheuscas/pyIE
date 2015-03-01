# *-* coding:utf-8 *-*
"""Module states Alagoas"""


def start(st_reg_number):
    """Checks the number valiaty for the Alagoas state"""

    if len(st_reg_number) > 9:
        return False

    if len(st_reg_number) < 9:
        return False

    if st_reg_number[0:2] != "24":
        return False

    if st_reg_number[2] not in ['0', '3', '5', '7', '8']:
        return False

    aux = 9
    sum_total = 0
    for i in range(len(st_reg_number)-1):
        sum_total = sum_total + int(st_reg_number[i]) * aux
        aux -= 1

    product = sum_total * 10

    aux_2 = int(product/11)

    digit = product - aux_2 * 11

    if digit == 10:
        digit = 0

    return digit == int(st_reg_number[len(st_reg_number)-1])
