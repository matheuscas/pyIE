# *-* coding:utf-8 *-*
def check (st_reg_number):
	DIVISOR = 11
	if len(st_reg_number)>9:
		return False
	
	if len(st_reg_number)<9:
		return False

	if st_reg_number[0:2] != "03":
		return False
	
	aux = int(st_reg_number[0:len(st_reg_number)-2])
	
	if 3000000 < aux and aux < 3017001:
		p = 5
		d = 0

	if 3017000 < aux and aux < 3019023:
		p = 9
		d = 1	
	
	if aux > 3019022:
		p = 0
		d = 0

	sum = 0
    	for i in range(len(st_reg_number)-1):
        	sum = sum + int(st_reg_number[i]) * aux
		aux -= 1
	sum += p

    	rest_division = sum % DIVISOR
    	digit = DIVISOR - rest_division

	if digit == 10: 
		digit = 0

	if digit == 11: 
		digit = d
    		
	
	return digit == int(st_reg_number[len(st_reg_number)-1])
	

