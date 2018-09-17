# decorators are the functions that have as argument a function,
# and returns a third function.
# They are identified by an "@" symbol before the function defition
# They are useful to define if a function must be exectued or not.

# Decorators are the syntaxis-added syntactic sugar.

# Example: generate a function that is protected by a password 


def passwd(f):
	def wrapper(passwd):
		if passwd == 'allantheboss':
			return f()
		else: 
			print('Incorrect password')

	return wrapper


#this is the "decorator" encapsulating its behavior inside the function passwd
@passwd 
def protected():
	print('Your password is correct.')

if __name__ == '__main__':
	pwd = input('Iput password: ')
	protected(pwd)