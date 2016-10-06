from functools import reduce

def str2num(s):
		a={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':-1}[s]
		if a>=0:
			print(a)
			return(a)
		else:
			print(-1)
			return(-1)
def fn(x,y):
	return x*10+y
	
def str2float(L):
	lat=[j for j in map(str2num,L) if j>=0]
	#b=reduce(fn,map(str2num,L))
	b=reduce(fn,lat)
	for  i in range(len(L)):
		if L[i].isdigit()==False:
			return(b*(10**(-(len(L)-i-1))))
	
print('str2float(\'123.456\') =', str2float('123.456'))


