def valid(n1, n2, n3):
	#print(n1,n2,n3)
	if n1 == n2 == n3: return -1
	if n1 == n2: return ((n1, n3), (n3, n1))
	if n1 == n3: return ((n1, n2), (n2, n1))
	if n2 == n3: return ((n1, n3), (n3, n1))

	return -1
	
def check_sin(board):
	global sin
	
	for i in range(3):
		if board[i][0] == board[i][1] == board[i][2]: sin.add(board[i][0])
		if board[0][i] == board[1][i] == board[2][i]: sin.add(board[0][i])
	if board[0][0] == board[1][1] == board[2][2]: sin.add(board[0][0])
	if board[0][2] == board[1][1] == board[2][0]: sin.add(board[1][1])
	

def check_dou(board):
	global dou
	
	for i in range(3):
		temp1 = valid(board[i][0], board[i][1], board[i][2])
		temp2 = valid(board[0][i], board[1][i], board[2][i])
		if temp1 != -1: 
			dou.add(temp1[0])
			dou.add(temp1[1])
		if temp2 != -1: 
			dou.add(temp2[0])
			dou.add(temp2[1])
	if valid(board[0][0], board[1][1], board[2][2]) != -1: 
		dou.add(valid(board[0][0], board[1][1], board[2][2])[0])
		dou.add(valid(board[0][0], board[1][1], board[2][2])[1])
	if valid(board[0][2], board[1][1], board[2][0]) != -1: 
		dou.add(valid(board[0][2], board[1][1], board[2][0])[0])
		dou.add(valid(board[0][2], board[1][1], board[2][0])[1])
	
	

lines = open('tttt.in').read().strip().split('\n')
board = list(map(list, lines))

sin = set()
dou = set()
check_sin(board)
check_dou(board)
print(len(sin))
print(len(dou) // 2)
#print(sin, dou)
file = open('tttt.out', 'w')
file.write(str(len(sin)) + '\n' + str(len(dou) // 2))
file.close()
