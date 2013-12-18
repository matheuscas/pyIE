# *-* coding:utf-8 *-*
def check (st_reg_number):

	DIVISOR = 11

	weight = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

	if len(st_reg_number) != 9 and len(st_reg_number) != 14:
		return False
	
	if len(st_reg_number) == 9:
		sum = 0
		peso = 6
		for i in range(3,len(st_reg_number)-1):
			sum = sum + int(st_reg_number[i]) * peso
			peso = peso - 1

		rest_division = sum % DIVISOR
	    	digit = DIVISOR - rest_division
		
		if digit == 10:
			digit = 0

		if digit == 11:
			digit = 1

		return digit == int(st_reg_number[len(st_reg_number)-1])	

	else:
		sum = 0
		for i in range(len(st_reg_number)-1):
			sum = sum + int(st_reg_number[i]) * weight[i]
			
		rest_division = sum % DIVISOR
	    	digit = DIVISOR - rest_division
		
		if digit == 10:
			digit = 0

		if digit == 11:
			digit = 1

		return digit == int(st_reg_number[len(st_reg_number)-1])
