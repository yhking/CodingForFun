# encoding: utf-8

def dec_to(n, m):
	s = ""
	while(n != 0):
		s += str(n % m)
		n //= m
	return s
	
def is_real(n):
	N = len(n)
	M = N//2
	i=0
	while(i != M):
		if n[i] != n[-(i+1)]:
			return False
		i += 1
	return True
			
	

if __name__ == "__main__":
	n = 10
	while(True):
		if is_real(str(n)) and is_real(dec_to(n,2)) and is_real(dec_to(n,8)):
			break
		else:
			n += 1
	print(n)
	print(dec_to(n,2))
	print(dec_to(n,8))