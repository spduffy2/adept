import math

class AStar:
	@staticmethod
	def aStar(start, goal, submaps):
		goal = (math.floor(goal[0]/32), math.floor(goal[1]/32))
		start = Square((math.floor(start[0]/32), math.floor(start[1]/32)), 0, None, goal)

		openSet = [start]
		closedSet = []
		nonViable = []

		for submap in submaps:
			pos = (math.floor(submap.pos[0]/32), math.floor(submap.pos[1]/32))
			for tile in submap.tileMap:
				if tile.collisionEnabled:
					nonViable.append((pos[0] + tile.pos[0], pos[1] + tile.pos[1]))

		while len(openSet) != 0 and openSet[-1].pos != goal:
			print "trying"
			current = openSet.pop()
			closedSet.append(current)
			neighbors = [(current.pos[0] + 1, current.pos[1]), (current.pos[0] - 1, current.pos[1]), (current.pos[0], current.pos[1] + 1), (current.pos[0], current.pos[1] - 1)]
			for neighbor in neighbors:
				if neighbor not in nonViable:
					cost = current.g + 1
					inSet = False
					for item in openSet:
						if item.pos == neighbor:
							if cost < item.g:
								openSet.remove(item)
							else:
								inSet = True
					for item in closedSet: # Technically should never happen
						if item.pos == neighbor:
							if cost < item.g:
								closedSet.remove(item)
							else:
								inSet = True
					if not inSet:
						newNeighbor = Square(neighbor, cost, current, goal)
						if len(openSet) == 0:
							openSet.append(newNeighbor)
							continue
						index = len(openSet) - 1
						relCost = openSet[index].f
						while relCost < newNeighbor.f and index > 0:
							index = index - 1
							relCost = openSet[index].f
						if relCost < openSet[index]:
							index = index - 1
						openSet.insert(index + 1, newNeighbor)

		if openSet[-1].pos != goal: # No path found
			print "failed"
			return None

		print "trying really hard"
		tracedPath = [openSet[-1]]
		print "where"
		positionPath = [openSet[-1].pos]
		print "does"
		while tracedPath[0].parent is not None:
			print "this"
			tracedPath.insert(0, tracedPath[0].parent)
			print "crash"
			positionPath.insert(0, tracedPath[0].pos)
			print "?"

		print "succeeded"
		return positionPath



class Square:
	def __init__(self, pos, g, parent, goal):
		self.pos = pos
		self.g = g
		self.h = self.getHeuristic(goal)
		self.f = self.g + self.h
		self.parent = parent

	def getHeuristic(self, goal):
		return math.hypot(goal[0] - self.pos[0], goal[1] - self.pos[1])