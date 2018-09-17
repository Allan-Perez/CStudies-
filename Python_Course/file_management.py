# Openning a lot of files is dangerous if we don't 
# manage them wisely. We have to close each after we are done

file = 'file.txt'
mode = 'r'

def files(file, mode_):
	with open(file, mode_) as f:
		if mode_ == 'r':
			read_my_file(f)
		elif mode_ == 'w':
			write_my_file(f,10)

def read_my_file(f):
	if(!isinstance(f, str)):
		raise Exception("The first argument of function write_my_file must be a string")
	lines = f.readlines()
	counter = 0
	for line in lines:
		print(line)
		# counter += line.count('whatever')

def write_my_file(f, l):
	if(!isinstance(l, int)):
		raise Exception("The second argument of function write_my_file must be an integer")
	if(!isinstance(f, str)):
		raise Exception("The first argument of function write_my_file must be a string")
	for i in range(l):
		f.write('Hello')

if __name__ == '__main__':
	files(file, mode)