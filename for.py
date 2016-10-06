
n=0
names={'Michael':35, 'Bob':90, 'Tracy':100}
#s1=input('the first:')
#s2=input('the second:')
#s3=input('the thrid:')
#score=[int(s1),int(s2),int(s3)]
#names['Michael']=float(s1)
score=[input('the first:'),input('the second:'),input('the thrid:')]
for name in names:
	names[name]=score[n]
	n=n+1
	print(name)
	#b=name
	#a=names[name]
	print(names[name])
