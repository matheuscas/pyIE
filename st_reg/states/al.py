# *-* coding:utf-8 *-*
def check (st_reg_number):
	if len(st_reg_number)>9:
		return False
	
	if len(st_reg_number)<9:
		return False

	if st_reg_number[0:2] != "24":
		return False
	
	if st_reg_number[2] not in ['0', '3', '5', '7', '8']:
		return False
	
	aux = 9	
	sum = 0
    	for i in range(len(st_reg_number)-1):	
		sum = sum + int(st_reg_number[i]) * aux
		aux -= 1
		
	product = sum * 10
	
	aux_2 = int(product/11)
	
	digit = product - aux_2 * 11
	
	if digit == 10:
		digit = 0

	return digit == int(st_reg_number[len(st_reg_number)-1])
		
	

