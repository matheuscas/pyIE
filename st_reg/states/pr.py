# *-* coding:utf-8 *-*
def check (st_reg_number):

	DIVISOR = 11

	weights_first = [3, 2, 7, 6, 5, 4, 3, 2 ]
	weights_secund = [4, 3, 2, 7, 6, 5, 4, 3, 2]

	if len(st_reg_number)>10:
		return False
	
	if len(st_reg_number)<10:
		return False

	sum = 0
	for i in range(len(st_reg_number)-2):
		sum = sum + int(st_reg_number[i]) * weights_first[i]
	
    	rest_division = sum % DIVISOR	
	digit_first = DIVISOR - rest_division
	
	if digit_first == 10 or digit_first == 11:
		digit_first = 0

	num = 0
	peso = 9
	mult = 100000000
    	for i in range(len(st_reg_number)-2):
		num = num + int(st_reg_number[i]) * mult
		mult = mult/10

	num = num + digit_first
	
	if num<10000000:
		new_st = str('0') + str(num)
	else:
		new_st = str(num)
	
	sum = 0
    	for i in range(len(new_st)):
		sum = sum + int(new_st[i]) * weights_secund[i]
	
	rest_division = sum % DIVISOR
    	digit_secund = DIVISOR - rest_division
	
	if digit_secund == 10 or digit_secund == 11:
		digit_secund = 0

	if digit_secund == int(st_reg_number[len(st_reg_number)-1]) and digit_first == int(st_reg_number[len(st_reg_number)-2]):
		return True
	else:
		return False
