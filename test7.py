from functools import reduce

def iter():
	n=1
	while True:
		n=n+1
		yield n
		
def divisible(m):
	return lambda x:x%m>0
	
def primes():
	#yield 2
	begin=iter()
	while True:
		n=next(begin)
		yield n
		begin=filter(divisible(n),begin)
		
for n in primes():
	if n<1000:
		print(n)
	else:
		break
	
