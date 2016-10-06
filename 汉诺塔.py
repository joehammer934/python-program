def mov(n,a,b,c):
	if n==1:
		print(a,'->',c)
	else:
		mov(n-1,a,c,b)
		mov(1,a,b,c)
		mov(n-1,b,a,c)

n=int(input('需要移动的盘子总数:'))
a=input('原始位置：')
b=input('过渡位置：')
c=input('目标位置：')
mov(n,a,b,c)
