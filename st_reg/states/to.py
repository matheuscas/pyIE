# *-* coding:utf-8 *-*
def check (st_reg_number):

	DIVISOR = 11

	if len(st_reg_number)>11:
		return False
	
	if len(st_reg_number)<11:
		return False

	if st_reg_number[2:4] not in ['01', '02', '03', '99']:
		return False

	sum = 0
	peso = 9
    	for i in range(len(st_reg_number)-1):
		if i != 2 and i != 3:
			sum = sum + int(st_reg_number[i]) * peso
			peso = peso - 1

	rest_division = sum % DIVISOR
    	digit = DIVISOR - rest_division	
	
	if rest_division < 2:
		digit = 0

	return digit == int(st_reg_number[len(st_reg_number)-1])
