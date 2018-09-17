# Naive algorithm for multiplying two numbers
# use it with args
import sys
import time

def naive(a,b):
	x = a
	y = b
	z = 0
	while y > 0:
		z = z + x
		y = y - 1
	return z

def main(func):
	if(len(sys.argv) < 3):
		raise Exception("Pass me args to multiply!")
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	init = time.time()
	z = func(a,b)
	end = time.time()
	print("Solution: ", z)
	if (end - init) < 1e-3:
		print("Running time: %.5g seconds" % (end - init) )
	else:
		print("Running time: %.5f seconds" % (end - init) )
if __name__ == '__main__':
	main(naive)