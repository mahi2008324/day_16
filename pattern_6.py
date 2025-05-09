for i in range(9):
	for j in range(8):
		if j-i==3 or i+j==11:
			print(">",end=" ")
		else:
			print(" ",end=" ")
	print()
		