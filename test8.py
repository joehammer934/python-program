from functools import reduce

def is_palindrome(n):
	b=n
	a=0
	while n/10>0:
		a=a*10+(n%10)
		n=int(n/10)
	if n/10==0:
		a=a+n
		#return a
		if a==b:
			return a
		
output = filter(is_palindrome, range(1, 10000))
print(list(output))
#print(is_palindrome(123))