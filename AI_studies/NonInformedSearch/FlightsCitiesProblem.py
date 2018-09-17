from BreadthFirstSearch import BreadthFirstSearch
import DepthFirstSearch as DFS
import UniformCostSearch as UCS
from tree import StaticNode

def backTrack(aim_node):
	if aim_node == False:
		print("Given method hasn't found any solution...")
		return
	i_node =aim_node
	path = []
	while i_node._father != None:
		path.append(i_node._state)
		i_node = i_node._father
	path.append(init_state)
	path.reverse()
	print("Path to the solution: ", path)

def findSolution(init_state, aim_state, transitionOps, searchMethod, mState_mNodes):
	aim_node = searchMethod(init_state, aim_state, transitionOps, mState_mNodes=mState_mNodes)

	backTrack(aim_node)

def findSolutionLimit(init_state, aim_state, transitionOps, mState_mNodes, limit):
	init_node = StaticNode(init_state, transitionOps=transitionOps, mState_mNodes=mState_mNodes)
	visited_nodes = set()
	aim_node = DFS.DepthLimitedSearch(init_node, aim_state, visited_nodes, limit)
	if aim_node == False:
		print("DLS hasn't found any solution.")
		return
	backTrack(aim_node)

def findSolutionWeighted(init_state, aim_state, transitionOps, searchMethod, mState_mNodes, weightsOps):
	aim_node = searchMethod(init_state, aim_state, transitionOps, mState_mNodes, weightsOps)
	print("Cost: ", aim_node._weight)
	backTrack(aim_node)
if __name__ == '__main__':
	# Given an origin city and a destiny city, 
	# find the route that has the least possible number of hops.
	# This problem will be tracted ignoring the distances and time schedules.
	# Goal: minimize the number of hops.

	init_state = 'Malaga'
	aim_state = 'Santiago'
	transitionOps = [lambda x: 
	{
		'Malaga':{'Salamanca', 'Madrid', 'Barcelona'},
		'Sevilla':{'Santiago', 'Madrid'},
		'Granada':{'Valencia'},
		'Valencia':{'Barcelona'},
		'Madrid':{'Malaga', 'Salamanca', 'Sevilla', 'Barcelona', 'Santander'},
		'Salamanca':{'Malaga', 'Madrid'},
		'Santiago':{'Sevilla', 'Santander', 'Barcelona'},
		'Santander':{'Santiago', 'Madrid'},
		'Zaragoza':{'Barcelona'},
		'Barcelona':{'Madrid', 'Malaga', 'Zaragoza', 'Santiago', 'Valencia'}
	}[x]]

	wTransitionOps = [lambda x: {
		'Malaga':{'Granada':125, 'Madrid':513},
		'Sevilla':{'Madrid':514},
		'Granada':{'Valencia':491, 'Madrid':423, 'Malaga':125},
		'Valencia':{'Barcelona':346, 'Granada':491, 'Madrid':356, 'Zaragoza':309},
		'Madrid':{'Malaga':513, 'Salamanca':203, 'Sevilla':514, 'Barcelona':603, \
			'Santander':437, 'Valencia':356, 'Zaragoza':313, \
			'Santiago':599, 'Granada':423},
		'Salamanca':{'Santiago':390, 'Madrid':203},
		'Santiago':{'Salamanca':390, 'Madrid':599},
		'Santander':{'Madrid':437, 'Zaragoza':394},
		'Zaragoza':{'Barcelona':296, 'Valencia':309, 'Madrid':313},
		'Barcelona':{'Madrid':603, 'Zaragoza':296, 'Valencia':346}
	}[x]]

	weightsOp = (lambda x, y: {
		'Malaga':{'Granada':125, 'Madrid':513},
		'Sevilla':{'Madrid':514},
		'Granada':{'Valencia':491, 'Madrid':423, 'Malaga':125},
		'Valencia':{'Barcelona':346, 'Granada':491, 'Madrid':356, 'Zaragoza':309},
		'Madrid':{'Malaga':513, 'Salamanca':203, 'Sevilla':514, 'Barcelona':603, \
			'Santander':437, 'Valencia':356, 'Zaragoza':313, \
			'Santiago':599, 'Granada':423},
		'Salamanca':{'Santiago':390, 'Madrid':203},
		'Santiago':{'Salamanca':390, 'Madrid':599},
		'Santander':{'Madrid':437, 'Zaragoza':394},
		'Zaragoza':{'Barcelona':296, 'Valencia':309, 'Madrid':313},
		'Barcelona':{'Madrid':603, 'Zaragoza':296, 'Valencia':346}
	}[x][y])


	print("BFS method:")
	findSolution(init_state, aim_state, transitionOps, BreadthFirstSearch, mState_mNodes=True)

	print("DFS method: ")
	findSolution(init_state, aim_state, transitionOps, DFS.DepthFirstSearch, mState_mNodes=True)	

	print("DLS method: ")
	findSolutionLimit(init_state, aim_state, transitionOps, mState_mNodes=True, limit=3)

	print("IDDFS method: ")
	findSolution(init_state, aim_state, transitionOps, DFS.IterativeDeepeningDepthFirstSearch, mState_mNodes=True)

	print("Weighted UCS method (Goal: Path with lowest cost) : ")
	findSolutionWeighted(init_state, aim_state, wTransitionOps, UCS.UniformCostSearch, mState_mNodes=True, weightsOps=weightsOp)
