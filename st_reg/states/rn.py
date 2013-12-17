# *-* coding:utf-8 *-*
def check (st_reg_number):

	DIVISOR = 11

	if len(st_reg_number)>10:
		return False
	
	if len(st_reg_number)<9:
		return False

	if st_reg_number[0:2] != "20":
		return False
	
	sum = 0
	peso = len(st_reg_number) # o peso pode ser 9 ou 10
    	for i in range(len(st_reg_number)-1):
		sum = sum + int(st_reg_number[i]) * peso
		peso = peso -1
	
	mult = sum * 10
	digit = mult % DIVISOR
	
	if digit == 10:
		digit = 0

	return digit == int(st_reg_number[len(st_reg_number)-1])
