import queue 
Queue = queue.Queue

class StaticNode:
	"""
	Representation of a node in a graph.
	The sense of Static is because the data that is defined is 
	what is used. It won't be updated, neither appended, nor flushed. 
	It has to represent:
		- The sate (get and set)
		- The offspring nodes (get and set)
		- The father node (get and set)
		- Weight (optional) (get and set)
		- Transition operations (actions to generate new offspring)
	Other utility methods:
		- compare: Returns ture if state of object node and parameter node are the same. 
		- in_list: Determines whether self node is in a list
		- set_offspring: sets offspring and updates each offspring node's data of father. 
		- produce_offspring: from transitionOps it produces new son nodes.
	"""
	def __init__(self, state, offspring=None, father=None, weight=None, transitionOps=None, mState_mNodes=False):
		if(transitionOps == None) :
			raise Exception("Node must have a transition operation.")
		self._state  = state
		self._offspring = offspring
		self._father = father
		self._weight = weight 
		self._transitionOps = transitionOps
		self._multipleStatesAreMultipleNodes = mState_mNodes

	def produce_offspring(self):
		offspring = []
		for transitionOp in self._transitionOps:
			node_states = transitionOp(self._state)
			if self._multipleStatesAreMultipleNodes:
				for node_state in node_states:
					offspring.append(StaticNode(node_state, transitionOps=self._transitionOps, 
						mState_mNodes=self._multipleStatesAreMultipleNodes))
			else: 
				offspring.append(StaticNode(node_states, transitionOps=self._transitionOps, 
					mState_mNodes=self._multipleStatesAreMultipleNodes))
		self.set_offspring(offspring)
		return offspring

	def set_offspring(self, offspring):
		self._offspring = offspring
		for son in offspring:
			son._father = self

	def set_weights(self, weightOp):
		self._weight = weightOp(self._father._state, self._state) + self._father._weight

	def compare(self, onode):
		return self._state == onode._state

	def in_list(self, node_list):
		return self._state in [n._state for n in node_list]