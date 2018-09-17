from tree import StaticNode

def compare(x, y):
	return x._weight - y._weight

def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0  
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K


def UniformCostSearch(init_state, aim_state, transitionOps, mState_mNodes, weightOps):
	init_node = StaticNode(init_state, transitionOps=transitionOps, mState_mNodes=mState_mNodes)
	init_node._weight = 0
	frontier_nodes = []
	visited_nodes = set()
	frontier_nodes.append(init_node)

	while len(frontier_nodes) > 0:
		frontier_nodes = sorted(frontier_nodes, key=cmp_to_key(compare))
		exploring_node = frontier_nodes.pop(0)
		visited_nodes.update([exploring_node])
		if exploring_node._state == aim_state:
			return exploring_node 

		offspring_nodes = exploring_node.produce_offspring()
		for son_node in offspring_nodes:
			son_node.set_weights(weightOps)
			if not son_node.in_list(list(visited_nodes)):
				if son_node.in_list(frontier_nodes):
					i = 0
					for node in frontier_nodes:	
						if son_node.compare(node) and son_node._weight < node._weight:
							frontier_nodes.pop(i)
							frontier_nodes.append(son_node)
						i +=1


				else:
					frontier_nodes.append(son_node)



if __name__ == '__main__':
	main()