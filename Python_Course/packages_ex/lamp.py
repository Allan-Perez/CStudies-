class Lamp:
	"""docstring for Lamp"""
	_LAMP = ['''
             ,-.
            (   )
             \ /
            _|=|_
           |_____|

    ''','''
              .
         .    |    ,
          \   '   /
           ` ,-. '
        --- (   ) ---
             \ /
            _|=|_
           |_____|
        ''']
	def __init__(self, turned_on_init):
		self._turned_on = turned_on_init

	def switch_lamp(self):
		if(self._turned_on):
			self._turned_on = False
		else:
			self._turned_on = True

	def print_lamp(self):
		print(self._LAMP[self._turned_on])

    