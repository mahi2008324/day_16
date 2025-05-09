for i in range(7):
	for j in range(7):
		if i==3 or i==6 or j-i==3 or i+j==3:
			print("*",end=" ")
		elif j==2 and i>2 or j==4 and i>2:
			print("*",end=" ")
		elif (j==0 or j==6) and i>2:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()
		