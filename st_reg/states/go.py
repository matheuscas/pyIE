def check(st_reg_number):
	weights = [9, 8, 7, 6, 5, 4, 3, 2]
	number_state_registration = st_reg_number[0:len(st_reg_number) - 1]
	digit_state_registration = st_reg_number[-1]

	
	if st_reg_number[0:2] not in ['10', '11', '12']:
		return False

	if len(st_reg_number) != 9:
		return False

	sum = 0

	for i in weights:
		sum = sum + i * (int(number_state_registration[-i+1]))
		

	if sum % 11 == 0:

		return '0' == digit_state_registration

	elif sum % 11 == 1 and (int(number_state_registration) >= 10103105  and number_state_registration <= 10119997):

		return '1' == digit_state_registration

	elif sum % 11 == 1:

		return '0' == digit_state_registration

	else:

		digit_check = 11 - sum % 11

		return digit_state_registration == str(digit_check)

	

	if number_state_registration == '11094402' and (number_state_registration == '1' or number_state_registration == '0'):
		return True

