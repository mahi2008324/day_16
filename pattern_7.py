for i in range(7):
	for j in range(10):
		if j-i==6 or i+j==12:
			print("*",end=" ")
		elif (i==2 or i==4) and j<7:
			print("*",end=" ")
		elif j==6 and i!=3:
			print("*",end=" ")
		elif i==3 and j==0:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()