from tree import StaticNode as Node
import queue

def DepthFirstSearch(init_state, aim_state, transitionOps, mState_mNodes=False):
	visited_nodes  = set()
	frontier_nodes = queue.LifoQueue()
	frontier_nodes.put(Node(init_state, transitionOps=transitionOps, mState_mNodes=mState_mNodes)) 
	while frontier_nodes.qsize()>0:
		exploring_node = frontier_nodes.get()
		visited_nodes.update([exploring_node])
		if exploring_node._state == aim_state:
			return exploring_node 
		offspring_nodes = exploring_node.produce_offspring()

		for son_node in offspring_nodes:
			if not son_node.in_list(list(visited_nodes)) and  \
			   not son_node.in_list(list(frontier_nodes.queue)):
				frontier_nodes.put(son_node)


	
def DepthLimitedSearch(exploring_node, aim_state, visited_nodes, limit):
	if limit > 0:
		visited_nodes.update([exploring_node])
		if exploring_node._state == aim_state: 
			return exploring_node
		offspring_nodes = exploring_node.produce_offspring()
		for son_node in offspring_nodes: 
			if not son_node.in_list(visited_nodes):
				return DepthLimitedSearch(son_node, aim_state, visited_nodes, limit-1)
		return DepthLimitedSearch(exploring_node._father, aim_state, visited_nodes, limit+1)
	return False # Limit exhausted and solution not found		

def IterativeDeepeningDepthFirstSearch(init_state, aim_state, transitionOps, mState_mNodes=False, iterRange=100):
	
	init_node = Node(init_state, transitionOps=transitionOps, mState_mNodes=mState_mNodes)
	for limit in range(iterRange):
		visited_nodes = set()
		solution = DepthLimitedSearch(init_node, aim_state, visited_nodes, limit)
		if solution != False:
			return solution
	return False