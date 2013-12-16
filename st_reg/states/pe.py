# *-* coding:utf-8 *-*
def check (st_reg_number):

	DIVISOR = 11

	if len(st_reg_number)>9:
		return False
	
	if len(st_reg_number)<9:
		return False

	sum = 0
	peso = 8
    	for i in range(len(st_reg_number)-2):
		sum = sum + int(st_reg_number[i]) * peso
		peso = peso - 1

    	rest_division = sum % DIVISOR
    	digit_first = DIVISOR - rest_division	
	
	if rest_division < 2:
		digit_first = 0

	if rest_division > 1:
		digit_first = 11 - rest_division

	num = 0
	peso = 9
	mult = 10000000
    	for i in range(len(st_reg_number)-2):
		num = num + int(st_reg_number[i]) * mult
		mult = mult/10

	num = num + digit_first

	new_st = str(num)
	sum = 0
	peso = 9
    	for i in range(len(new_st)-1):
		sum = sum + int(new_st[i]) * peso
		peso = peso - 1
	
	rest_division = sum % DIVISOR
    	
	if rest_division < 2:
		digit_secund = 0

	if rest_division > 1:
		digit_secund = DIVISOR - rest_division

	if digit_secund == int(st_reg_number[len(st_reg_number)-1]) and digit_first == int(st_reg_number[len(st_reg_number)-2]):
		return True
	else:
		return False
