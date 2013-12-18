def check(st_reg_number):
	#st_reg_number = str(st_reg_number)
	weights = [9, 8, 7, 6, 5, 4, 3, 2]
	digit_state_registration = st_reg_number[-1]

	if len(st_reg_number ) != 9:
		return False

	sum = 0

	for i in range(0,8):
		sum = sum + weights[i] * int(st_reg_number[i])
		print i, st_reg_number[-i], sum

	if sum % 11 == 0:
		return digit_state_registration[-1] == '0'

	digit_check = 11 - sum % 11

	

	return str(digit_check) == digit_state_registration