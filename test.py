h=input('height:')
w=input('weight:')
height=1.75
weight=80.5
#bmi=weight/(height**2)
a= float (w)
b=float(h)
bmi=a/(b**2)
if bmi<18.5:
	print('过轻')
elif bmi<25:
	print('正常')
elif bmi<28:
	print('过重')
elif bmi<32:
	print('肥胖')
elif bmi>=32:
	print('严重肥胖')