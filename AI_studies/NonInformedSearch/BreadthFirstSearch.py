from tree import StaticNode as Node
import queue

def BreadthFirstSearch(init_state, aim_state, transitionOps, mState_mNodes=False):
	visited_nodes  = set()
	frontier_nodes = queue.Queue()
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


	

