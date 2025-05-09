#,<,>,= 
for i in range(10):
	for j in range(8):
		if j==2 or j==5 or i==3 or i==6:
			print("#",end=" ")
		else:
			print(" ",end=" ")
	print()