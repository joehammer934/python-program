
import math

def quadratic(s0,s1,s2):
	a=float (s0)
	b=float (s1)
	c=float (s2)
	return ((-b+math.sqrt(b*b-4*a*c))/(2*a),(-b-math.sqrt(b*b-4*a*c))/(2*a))
def nop():
	pass
	
s0=input('参数a是:')
s1=input('参数b是:')
s2=input('参数c是:')
r=quadratic(s0,s1,s2)
print (r)
