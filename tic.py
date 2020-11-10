n = 1
mat = [['-','-','-'] for i in range(3)]
acq = [1,2,3,4,5,6,7,8,9]
while n<=9:
	n += 1
	for i in mat:
		print(i[0],'|',i[1],'|',i[2])
	if n%2==0:
		pos = int(input("\nO's turn: "))
		if pos%3==0:
			i = pos//3-1
		else:
			i = pos//3
		if pos in acq:
			mat[i][pos%3-1] = 'O'
			acq.remove(pos)
		else:
			print("\nIts already filled")
			n -= 1
	else:
		pos = int(input("\nX's turn: "))
		if pos%3==0:
			i = pos//3-1
		else:
			i = pos//3
		if pos in acq:
			mat[i][pos%3-1] = 'X'
			acq.remove(pos)
		else:
			print("\nIts already filled")
			n -= 1
	print()
	inv = list(zip(*mat))
	if mat[0][0]==mat[0][1]==mat[0][2]=='O' or mat[1][0]==mat[1][1]==mat[1][2]=='O' or mat[2][0]==mat[2][1]==mat[2][2]=='O' or mat[0][0]==mat[1][1]==mat[2][2]=='O' or mat[0][2]==mat[1][1]==mat[2][0]=='O' or inv[0][0]==inv[0][1]==inv[0][2]=='O' or inv[1][0]==inv[1][1]==inv[1][2]=='O' or inv[2][0]==inv[2][1]==inv[2][2]=='O':
		for i in mat:
			print(i[0],'|',i[1],'|',i[2])
		print("\nGame Won by O")
		break
	elif mat[0][0]==mat[0][1]==mat[0][2]=='X' or mat[1][0]==mat[1][1]==mat[1][2]=='X' or mat[2][0]==mat[2][1]==mat[2][2]=='X' or mat[0][0]==mat[1][1]==mat[2][2]=='X' or mat[0][2]==mat[1][1]==mat[2][0]=='X' or inv[0][0]==inv[0][1]==inv[0][2]=='X' or inv[1][0]==inv[1][1]==inv[1][2]=='X' or inv[2][0]==inv[2][1]==inv[2][2]=='X':
		for i in mat:
			print(i[0],'|',i[1],'|',i[2])
		print("\nGame Won by X")
		break
	elif n>9:
		for i in mat:
			print(i[0],'|',i[1],'|',i[2])
		print("\nMatch is Tied")

