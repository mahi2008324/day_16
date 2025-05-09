for i in range(10):
	for j in range(7):
		if (j==2 or j==4) and i>2:
			print("*",end=" ")
		elif i==3 and j!=3:
			print("*",end=" ")
		elif (i+j==3 or j-i==3) or (i==9 and j==3):
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()