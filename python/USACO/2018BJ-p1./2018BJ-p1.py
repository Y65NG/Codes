#1: left in; 2: right in; 3: both in; 0: both out
def x_in_range():
	if f_board[0] ># m_board[0] and f_board[2] < m_board[2]: return 3
	elif f_board[0] <= m_board[0]: return 

fin = open('billboard.in').read().strip().split('\n')
m_board, f_board = list(map(int, fin[0])), list(map(int, fin[1]))
width = m_board[2] - m_board[0]
height = m_board[3] - m_board[1]

if f_board[0] <= m_board[0] and f_board[2] >= m_board[2] and (f_board[1] in range(m_board[1], m_board[3] + 1) and not (f_board[1] and f_board[3] in range(m_board[1], m_board[3] + 1)):
	width -= abs()
