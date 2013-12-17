# *-* coding:utf-8 *-*
def check (st_reg_number):

	DIVISOR = 9

	if len(st_reg_number)>9:
		return False
	
	if len(st_reg_number)<9:
		return False

	if st_reg_number[0:2] != "24":
		return False

	sum = 0
	peso = 1
    	for i in range(len(st_reg_number)-1):
		sum = sum + int(st_reg_number[i]) * peso
		peso = peso + 1

	digit = sum % DIVISOR

	return digit == int(st_reg_number[len(st_reg_number)-1])

