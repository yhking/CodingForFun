# encoding: utf-8
	
def is_real(str_n):
	if str_n == str_n[::-1]:
		return True
	else:
		return False
			
	

if __name__ == "__main__":
	n = 11
	while(True):
		if is_real(str(n)) and is_real(bin(n)[2:]) and is_real(oct(n)[2:]):
			break
		else:
			n += 2 #奇数才有可能是回文数
	print(n)
	print(bin(n))
	print(oct(n))