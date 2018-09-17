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
