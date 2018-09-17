from BreadthFirstSearch import BreadthFirstSearch
from DepthFirstSearch import DepthFirstSearch

def findSolution(init_state, aim_state, transitionOps, solutionMethod):
	aim_node = solutionMethod(init_state, aim_state, transitionOps)
	i_node = aim_node
	path = []
	while i_node._father != None:
		path.append(i_node._state)
		i_node = i_node._father
	path.append(init_state)
	path.reverse()
	print("Path to the solution: ")
	print(path)

if __name__ == '__main__':
	# This is like a line puzzle where there're 4 pieces: 
	# 1  2  3  4  
	# We start from whatever state, and and up in the goal
	# state, which in this case is the same depicted above.
	# We use 3 actions: left swipe, middle swipe, right swipe. 
	init_state = [4,2,3,1]
	aim_state = [1,2,3,4]
	transitionOps = (lambda x : [x[1],x[0],x[2],x[3]],
					lambda x : [x[0],x[2],x[1],x[3]],
					lambda x : [x[0],x[1],x[3],x[2]])
	print('BFS: ')
	findSolution(init_state, aim_state, transitionOps,  BreadthFirstSearch)
	print('DFS: ')
	findSolution(init_state, aim_state, transitionOps,  DepthFirstSearch)
