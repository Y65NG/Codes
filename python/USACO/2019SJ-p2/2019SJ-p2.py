from collections import deque

lines = open('perimeter.in').read().strip().split('\n')
N, graph = int(lines[0]), lines[1:]

def bfs(graph, x, y):
	visited = set()
	
