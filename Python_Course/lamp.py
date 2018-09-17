


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


def main():
	my_super_lamp = Lamp(turned_on_init=True)

	while True:
		switch = input("Switch lamp [Y,n]? (Ctrl-C to end)" ).lower()

		if switch == 'y':
			if my_super_lamp._turned_on == False:
				my_super_lamp.switch_lamp()
			my_super_lamp.print_lamp()
		elif switch == 'n':
			if my_super_lamp._turned_on != False:
				my_super_lamp.switch_lamp()
			my_super_lamp.print_lamp()
		else:
			print('I couldn\'t understand {}. I can only read [Y,n]'.format(switch))


if __name__ == '__main__':
	main()

