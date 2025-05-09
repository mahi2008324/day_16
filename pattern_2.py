for i in range(6):
	for j in range(9):
		if i+j==9 or i-j==1 or (i+j==6 and i<3) or (j-i==2 and i<3) or (i==0 and j==7):
			print("*",end="  ")
		elif i==0 and j==1:
			print("*",end="  ")
		else:
			print(" ",end="  ")
	print("\n")