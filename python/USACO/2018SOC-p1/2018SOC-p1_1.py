import heapq

lines = open('sort.in').read().strip().split('\n')
N, arr = int(lines[0]), [-int(x) for x in lines[1:]]
poses = {}
for i in range(len(arr)):
	poses[arr[i]] = i
heapq.heapify(arr)
#print(arr, poses)

max_index = len(arr) - 1
count = 0
for max_index in range(len(arr) - 1, 0, -1):
	num = heapq.heappop(arr)
	
	count += max_index - poses[num] - (len(arr) - 1 - max_index)
	#print(max_index, num, poses[num], count)
print(count)
file = open('sort.out', 'w')
file.write(str(count))
file.close()
