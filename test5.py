from functools import reduce

def qiuji(x,y):
	return(x*y)

def prod(L):
	return reduce(qiuji,L)
	
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
