# *-* coding:utf-8 *-*
def check (st_reg_number):

	DIVISOR = 11

	weights_first = [1, 3, 4, 5, 6, 7, 8, 10]
	weights_secund = [3, 2, 10, 9, 8, 7, 6, 5, 4, 3, 2]

	if len(st_reg_number)>13:
		return False
	
	if len(st_reg_number)<12:
		return False

	if len(st_reg_number) == 12:
		sum = 0
		for i in range(len(st_reg_number)-4):
			sum = sum + int(st_reg_number[i]) * weights_first[i]

		rest_division = sum % DIVISOR
		digit_first = rest_division	

		if rest_division == 10:
			digit_first = 0

		num = 0
		peso = 9
		mult = 10000000000
	    	for i in range(len(st_reg_number)-1):
			if i == 8:
				num = num + digit_first * mult
			else:
				num = num + int(st_reg_number[i]) * mult
			mult = mult/10
	
		if num<10000000000:
			new_st = str('0') + str(num)
		else:
			new_st = str(num)

		sum = 0
		for i in range(len(new_st)):
			sum = sum + int(new_st[i]) * weights_secund[i]

		rest_division = sum % DIVISOR
		digit_secund = rest_division	

		if rest_division == 10:
			digit_secund = 0
	
		if digit_secund == int(st_reg_number[len(st_reg_number)-1]) and digit_first == int(st_reg_number[len(st_reg_number)-4]):
			return True
		else:
			return False

	else:
		if st_reg_number[0] != "P":
			return False

		sum = 0
		for i in range(1, 9):
			sum = sum + int(st_reg_number[i]) * weights_first[i-1]	
		
		digit = sum % DIVISOR	
	
		if digit == 10:
			digit = 0		
		
		return digit == int(st_reg_number[len(st_reg_number)-4])	
