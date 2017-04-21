#! /usr/bin/python3

import sys

statesVisited = 0

def getStart(S):
	lines = S.readlines()
	currentLine = lines[0].split(",")
	
	smf = currentLine[0]
	scf = currentLine[1]
	temp = currentLine[2].split("\n")
	sbf = temp[0]

	currentLine = lines[1].split(",")

	smn = currentLine[0]
	scn = currentLine[1]
	temp = currentLine[2].split("\n")
	sbn = temp[0]

	start = [smf, scf, sbf, smn, scn, sbn]

	return start

def getGoal(G):
	lines = G.readlines()
	currentLine = lines[0].split(",")

	gmf = currentLine[0]
	gcf = currentLine[1]
	temp = currentLine[2].split("\n")
	gbf = temp[0]

	currentLine = lines[1].split(",")

	gmn = currentLine[0]
	gcn = currentLine[1]
	temp = currentLine[2].split("\n")
	gbn = temp[0]

	goal = [gmf, gcf, gbf, gmn, gcn, gbn]

	return goal

def findSpot(value, current):
	i = 0
	if(len(current) == 0):
		return 0
	else:
		while current[i][1] < value:
			i += 1
	return i

def isReachable(cur, path):
	if len(path) == 0:
		return 1
	elif cur[2] == 1:
		if cur[0] == path[len(path)-1][0]+1 and cur[1] == path[len(path)-1][1] and cur[3] == path[len(path)-1][3]-1 and cur[4] == path[len(path)-1][4] and cur[2] == path[len(path)-1][5]:
			return 1
		elif cur[0] == path[len(path)-1][0]+2 and cur[1] == path[len(path)-1][1] and cur[3] == path[len(path)-1][3]-2 and cur[4] == path[len(path)-1][4] and cur[2] == path[len(path)-1][5]:
			return 1
	 	elif cur[0] == path[len(path)-1][0] and cur[1] == path[len(path)-1][1]+1 and cur[3] == path[len(path)-1][3] and cur[4] == path[len(path)-1][4]-1 and cur[2] == path[len(path)-1][5]:
			return 1
		elif cur[0] == path[len(path)-1][0]+1 and cur[1] == path[len(path)-1][1]+1 and cur[3] == path[len(path)-1][3]-1 and cur[4] == path[len(path)-1][4]-1 and cur[2] == path[len(path)-1][5]:
			return 1
		elif cur[0] == path[len(path)-1][0] and cur[1] == path[len(path)-1][1]+2 and cur[3] == path[len(path)-1][3] and cur[4] == path[len(path)-1][4]-2 and cur[2] == path[len(path)-1][5]:
			return 1
		else:
			return 0
	elif cur[2] == 0:
		if cur[0] == path[len(path)-1][0]-1 and cur[1] == path[len(path)-1][1] and cur[3] == path[len(path)-1][3]+1 and cur[4] == path[len(path)-1][4] and cur[2] == path[len(path)-1][5]:
			return 1
		elif cur[0] == path[len(path)-1][0]-2 and cur[1] == path[len(path)-1][1] and cur[3] == path[len(path)-1][3]+2 and cur[4] == path[len(path)-1][4] and cur[2] == path[len(path)-1][5]:
			return 1
		elif cur[0] == path[len(path)-1][0] and cur[1] == path[len(path)-1][1]-1 and cur[3] == path[len(path)-1][3] and cur[4] == path[len(path)-1][4]+1 and cur[2] == path[len(path)-1][5]:
			return 1
		elif cur[0] == path[len(path)-1][0]-1 and cur[1] == path[len(path)-1][1]-1 and cur[3] == path[len(path)-1][3]+1 and cur[4] == path[len(path)-1][4]+1 and cur[2] == path[len(path)-1][5]:
			return 1
		elif cur[0] == path[len(path)-1][0] and cur[1] == path[len(path)-1][1]-2 and cur[3] == path[len(path)-1][3] and cur[4] == path[len(path)-1][4]+2 and cur[2] == path[len(path)-1][5]:
			return 1
		else:
			return 0
	else:
		return 0

	return 0

def getPath(cur, visited, path, goal):
	if cur == goal:
		path.append(cur)
		return path
	elif isReachable(cur, path[:]):
		path.append(cur)
		for i in visited:
			new = visited.pop(0)
			newPath = getPath(new, visited[:], path[:], goal)
			if newPath != 0:
				return newPath
		return 0
	else:
		return 0
	
def bfs(start, goal, O):
	O.write("Breadth First Search\n")

	statesVisited = 0;
	current = []
	visited = []
	temp = []

	for i in start:
		temp.append(int(i))
	current.append(temp)
	temp = []
	for i in goal:
		temp.append(int(i))
	goal = temp
		
	while len(current) > 0:
		success = 0
		cur = current.pop(0)
		for i in visited:
			if i == cur:
				success = 1
				break
		if (cur[0] < cur[1] and cur[0] != 0) or (cur[3] < cur[4] and cur[3] != 0) or cur[0] < 0 or cur[1] < 0 or cur[3] < 0 or cur[4] < 0:
			success = 1

		if success == 0:
			statesVisited += 1
			visited.append(cur)
			if cur == goal:
				O.write('Goal Found\n')
				O.write('Final Number of States Visited: ' + str(statesVisited) + '\n')
				path = []
				cur = visited.pop(0)
				path = getPath(cur, visited[:], path[:], goal)
				O.write('Final Path\n')
				O.write('Length: ' + str(len(path)) + "\n")
				for i in path:
					O.write(str(i) + "\n")
					print str(i)
				return
			if cur[5] == 1:
				temp = [cur[0]+1, cur[1], 1, cur[3]-1, cur[4], 0]
				current.append(temp)
				temp = [cur[0]+2, cur[1], 1, cur[3]-2, cur[4], 0]
				current.append(temp)
				temp = [cur[0], cur[1]+1, 1, cur[3], cur[4]-1, 0]
				current.append(temp)
				temp = [cur[0]+1, cur[1]+1, 1, cur[3]-1, cur[4]-1, 0]
				current.append(temp)
				temp = [cur[0], cur[1]+2, 1, cur[3], cur[4]-2, 0]
				current.append(temp)
			elif cur[2] == 1:
				temp = [cur[0]-1, cur[1], 0, cur[3]+1, cur[4], 1]
				current.append(temp)
				temp = [cur[0]-2, cur[1], 0, cur[3]+2, cur[4], 1]
				current.append(temp)
				temp = [cur[0], cur[1]-1, 0, cur[3], cur[4]+1, 1]
				current.append(temp)
				temp = [cur[0]-1, cur[1]-1, 0, cur[3]+1, cur[4]+1, 1]
				current.append(temp)
				temp = [cur[0], cur[1]-2, 0, cur[3], cur[4]+2, 1]
				current.append(temp)

	return

def dfs(start, goal, O):
	O.write("Depth First Search\n")

	statesVisited = 0;
	current = []
	visited = []
	temp = []
	for i in start:
		temp.append(int(i))
	current.append(temp)
	temp = []
	for i in goal:
		temp.append(int(i))
	goal = temp
		
	while len(current) > 0:
		success = 0
		cur = current.pop(0)

		for i in visited:
			if i == cur:
				success = 1
				break
		if (cur[0] < cur[1] and cur[0] != 0) or (cur[3] < cur[4] and cur[3] != 0) or cur[0] < 0 or cur[1] < 0 or cur[3] < 0 or cur[4] < 0:
			success = 1

		if success == 0:
			statesVisited += 1
			visited.append(cur)
			#O.write(str(cur) + "\n")
			if cur == goal:
				O.write('Goal Found\n')
				O.write('Final Number of States Visited: ' + str(statesVisited) + '\n')
				path = []
				cur = visited.pop(0)
				path = getPath(cur, visited[:], path[:], goal)
				O.write('Final Path\n')
				O.write('Length: ' + str(len(path)) + "\n")
				for i in path:
					O.write(str(i) + "\n")
					print str(i)
				return
			if cur[5] == 1:
				temp = [cur[0]+1, cur[1], 1, cur[3]-1, cur[4], 0]
				current.insert(0, temp)
				temp = [cur[0]+2, cur[1], 1, cur[3]-2, cur[4], 0]
				current.insert(1, temp)
				temp = [cur[0], cur[1]+1, 1, cur[3], cur[4]-1, 0]
				current.insert(2, temp)
				temp = [cur[0]+1, cur[1]+1, 1, cur[3]-1, cur[4]-1, 0]
				current.insert(3, temp)
				temp = [cur[0], cur[1]+2, 1, cur[3], cur[4]-2, 0]
				current.insert(4, temp)
			elif cur[2] == 1:
				temp = [cur[0]-1, cur[1], 0, cur[3]+1, cur[4], 1]
				current.insert(0, temp)
				temp = [cur[0]-2, cur[1], 0, cur[3]+2, cur[4], 1]
				current.insert(1, temp)
				temp = [cur[0], cur[1]-1, 0, cur[3], cur[4]+1, 1]
				current.insert(2, temp)
				temp = [cur[0]-1, cur[1]-1, 0, cur[3]+1, cur[4]+1, 1]
				current.insert(3, temp)
				temp = [cur[0], cur[1]-2, 0, cur[3], cur[4]+2, 1]
				current.insert(4, temp)

	return

def iddfs(start, goal, O, current, visited, depth):
	global statesVisited

	if len(current) <= 0:
		O.write("No Goal Found\n")
		print "No Goal Found"
		return
	elif depth > 500:
		return
	else:
		success = 0
		cur = current.pop(0)
		for i in visited:
			if i == cur:
				success = 1
				break
		if(cur[0] < cur[1] and cur[0] != 0) or (cur[3] < cur[4] and cur[3] != 0) or cur[0] < 0 or cur[1] < 0 or cur[3] < 0 or cur[4] < 0:
			success = 1
		
		if success == 0:
			statesVisited += 1
			depth += 1
			visited.append(cur)
			if cur == goal:
				O.write("Goal Found\n")
				O.write("Final Number of States Visited: " + str(statesVisited) + "\n")
				path = []
				cur = visited.pop(0)
				path = getPath(cur, visited[:], path[:], goal)
				O.write("Final Patch\n")
				O.write('Length: ' + str(len(path)) + "\n")
				for i in path:
					O.write(str(i) + "\n")
					print str(i)
				return
			if cur[5] == 1:
				temp = [cur[0]+1, cur[1], 1, cur[3]-1, cur[4], 0]
				current.insert(0, temp)
				iddfs(start, goal, O, current, visited, depth)
				temp = [cur[0]+2, cur[1], 1, cur[3]-2, cur[4], 0]
				current.insert(0, temp)
				iddfs(start, goal, O, current, visited, depth)
				temp = [cur[0], cur[1]+1, 1, cur[3], cur[4]-1, 0]
				current.insert(0, temp)
				iddfs(start, goal, O, current, visited, depth)
				temp = [cur[0]+1, cur[1]+1, 1, cur[3]-1, cur[4]-1, 0]
				current.insert(0, temp)
				iddfs(start, goal, O, current, visited, depth)
				temp = [cur[0], cur[1]+2, 1, cur[3], cur[4]-2, 0]
				current.insert(0, temp)
				iddfs(start, goal, O, current, visited, depth)
			elif cur[2] == 1:
				temp = [cur[0]-1, cur[1], 0, cur[3]+1, cur[4], 1]
				current.insert(0, temp)
				iddfs(start, goal, O, current, visited, depth)
				temp = [cur[0]-2, cur[1], 0, cur[3]+2, cur[4], 1]
				current.insert(0, temp)
				iddfs(start, goal, O, current, visited, depth)
				temp = [cur[0], cur[1]-1, 0, cur[3], cur[4]+1, 1]
				current.insert(0, temp)
				iddfs(start, goal, O, current, visited, depth)
				temp = [cur[0]-1, cur[1]-1, 0, cur[3]+1, cur[4]+1, 1]
				current.insert(0, temp)
				iddfs(start, goal, O, current, visited, depth)
				temp = [cur[0], cur[1]-2, 0, cur[3], cur[4]+2, 1]
				current.insert(0, temp)
				iddfs(start, goal, O, current, visited, depth)

	return

def astar(start, goal, O):
	O.write("A STAR\n")

	statesVisited = 0;
	current = []
	visited = []
	temp = []
	for i in start:
		temp.append(int(i))
	tempAgain = []
	tempAgain.append(temp)
	temp = []
	temp.append(tempAgain[0][3] + tempAgain[0][4])
	tempAgain.append(temp)
	current.append(tempAgain)
	
	temp = []
	for i in goal:
		temp.append(int(i))
	goal = temp
	
	while len(current) > 0:
		success = 0
		cur = current.pop(0)

		for i in visited:
			if i == cur[0]:
				success = 1
				break

		if (cur[0][0] < cur[0][1] and cur[0][0] != 0) or (cur[0][3] < cur[0][4] and cur[0][3] != 0) or cur[0][0] < 0 or cur[0][1] < 0 or cur[0][3] < 0 or cur[0][4] < 0:
			success = 1

		if success == 0:
			statesVisited += 1
			visited.append(cur[0])
			#O.write(str(cur) + "\n")
			if cur[0] == goal:
				O.write('Goal Found\n')
				O.write('Final Number of States Visited: ' + str(statesVisited) + '\n')
				path = []
				cur = visited.pop(0)
				path = getPath(cur, visited[:], path[:], goal)
				O.write('Final Path\n')
				O.write('Length: ' + str(len(path)) + "\n")
				for i in path:
					O.write(str(i) + "\n")
					print str(i)
				return
			if cur[0][5] == 1:
				temp = [cur[0][0]+1, cur[0][1], 1, cur[0][3]-1, cur[0][4], 0]
				newTemp = []
				newTemp.append(temp)
				temp = []
				temp.append(cur[0][3] + cur[0][4] + 1)
				newTemp.append(temp)
				i = findSpot(newTemp[1][0], current)
				current.insert(i, newTemp)
				
				temp = [cur[0][0]+2, cur[0][1], 1, cur[0][3]-2, cur[0][4], 0]
				newTemp = []
				newTemp.append(temp)
				temp = []
				temp.append(cur[0][3] + cur[0][4] + 2)
				newTemp.append(temp)
				i = findSpot(newTemp[1][0], current)
				current.insert(i, newTemp)

				temp = [cur[0][0], cur[0][1]+1, 1, cur[0][3], cur[0][4]-1, 0]
				newTemp = []
				newTemp.append(temp)
				temp = []
				temp.append(cur[0][3] + cur[0][4] + 1)
				newTemp.append(temp)
				i = findSpot(newTemp[1][0], current)
				current.insert(i, newTemp)

				temp = [cur[0][0]+1, cur[0][1]+1, 1, cur[0][3]-1, cur[0][4]-1, 0]
				newTemp = []
				newTemp.append(temp)
				temp = []
				temp.append(cur[0][3] + cur[0][4] + 2)
				newTemp.append(temp)
				i = findSpot(newTemp[1][0], current)
				current.insert(i, newTemp)

				temp = [cur[0][0], cur[0][1]+2, 1, cur[0][3], cur[0][4]-2, 0]
				newTemp = []
				newTemp.append(temp)
				temp = []
				temp.append(cur[0][3] + cur[0][4] + 2)
				newTemp.append(temp)
				i = findSpot(newTemp[1][0], current)
				current.insert(i, newTemp)

			elif cur[0][2] == 1:
				temp = [cur[0][0]-1, cur[0][1], 0, cur[0][3]+1, cur[0][4], 1]
				newTemp = []
				newTemp.append(temp)
				temp = []
				temp.append(cur[0][3] + cur[0][4] + 1)
				newTemp.append(temp)
				i = findSpot(newTemp[1][0], current)
				current.insert(i, newTemp)

				temp = [cur[0][0]-2, cur[0][1], 0, cur[0][3]+2, cur[0][4], 1]
				newTemp = []
				newTemp.append(temp)
				temp = []
				temp.append(cur[0][3] + cur[0][4] + 2)
				newTemp.append(temp)
				i = findSpot(newTemp[1][0], current)
				current.insert(i, newTemp)

				temp = [cur[0][0], cur[0][1]-1, 0, cur[0][3], cur[0][4]+1, 1]	
				newTemp = []
				newTemp.append(temp)
				temp = []
				temp.append(cur[0][3] + cur[0][4] + 1)
				newTemp.append(temp)
				i = findSpot(newTemp[1][0], current)
				current.insert(i, newTemp)

				temp = [cur[0][0]-1, cur[0][1]-1, 0, cur[0][3]+1, cur[0][4]+1, 1]
				newTemp = []
				newTemp.append(temp)
				temp = []
				temp.append(cur[0][3] + cur[0][4] + 2)
				newTemp.append(temp)
				i = findSpot(newTemp[1][0], current)
				current.insert(i, newTemp)

				temp = [cur[0][0], cur[0][1]-2, 0, cur[0][3], cur[0][4]+2, 1]	
				newTemp = []
				newTemp.append(temp)
				temp = []
				temp.append(cur[0][3] + cur[0][4] + 2)
				newTemp.append(temp)
				i = findSpot(newTemp[1][0], current)
				current.insert(i, newTemp)

	return


if len(sys.argv) != 5:
	print('Proper Use: python ./mac.py <init state file> <goal state file> <mode> <output file>')
	quit()
else:
	print str(sys.argv)

S = open(sys.argv[1], "r")
G = open(sys.argv[2], "r")
mode = sys.argv[3]
O = open(sys.argv[4], "w")

start = getStart(S)
goal = getGoal(G)

print "Start State: " + str(start)
print "Goal State: " + str(goal)

if mode == "bfs":
	bfs(start, goal, O)
elif mode == "dfs":
	dfs(start, goal, O)
elif mode == "iddfs":
	statesVisited = 0;
	depth = 0
	current = []
	visited = []
	temp = []
	for i in start:
		temp.append(int(i))
	current.append(temp)
	temp = []
	for i in goal:
		temp.append(int(i))
	goal = temp
	current.append(start)
	O.write("Iterative Deepening Depth First Search\n")
	iddfs(start, goal, O, current, visited, depth)
elif mode == "astar":
	astar(start, goal, O)
else:
	print("Invalid Mode. Valid Modes Are: bfs, dfs, iddfs, astar")
	exit()


