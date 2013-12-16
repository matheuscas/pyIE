def check (st_reg_number ):
	weights = range(2,10)
	digit = st_reg_number[0:len(st_reg_number) - 1]
	controle_do_digito = 11
	check_digit = st_reg_number[-1:]

	sum = 0
	for i in weights: 			
		sum = sum + i * int(digit[i - 2])
	

	if sum < controle_do_digito:
		digit_calculated = 11 - sum

		return str(digit_calculated) == check_digit

	elif sum%11 <= 1:
		return '0' == check_digit

	else:
		digit_calculated = 11 - sum % 11
		return str(digit_calculated) == check_digit

	





