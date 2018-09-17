# Ancient Egyptian Multiplication
import sys
import time
from naive_function import main

def egypt_mult(a,b):
	x=a;y=b
	z = 0
	while x > 0:
		if x % 2 == 0 : z = z + x
		x = x >> 1
		y = y << 1
	return z


if __name__ == '__main__':
	main(egypt_mult)