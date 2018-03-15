x=input()
y=input()
if(y>x):
		(x,y)=(y,x)

while(x%y!=0):
	(x,y)=(y,x%y)

print("Gcd is {0}".format(y))
