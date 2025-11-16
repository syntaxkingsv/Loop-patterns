while True:	
	n=int(input("Enter number for factorial:"))
	f=1
	i=1
	while(i<=n):
		f=f*i
		i=i+1
	print(f)
	a=input("do you want to continue:").lower()
	if a=="yes":
		continue
	else:
		break
