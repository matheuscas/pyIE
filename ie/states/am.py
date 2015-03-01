# *-* coding:utf-8 *-*
"""Amazonas state module"""


def start(st_reg_number):
        """Checks the number valiaty for the Amazonas state"""
        weights = range(2, 10)
        digits = st_reg_number[0:len(st_reg_number) - 1]
        control_digit = 11
        check_digit = st_reg_number[-1:]

        if len(st_reg_number) != 9:
                return False

        sum_total = 0

        for i in weights:
                sum_total = sum_total + i * int(digits[i-2])

        if sum_total < control_digit:
                control_digit = 11 - sum_total
                return str(digit_calculated) == check_digit

        elif sum_total % 11 <= 1:
                return '0' == check_digit

        else:
                digit_calculated = 11 - sum_total % 11
                return str(digit_calculated) == check_digit
