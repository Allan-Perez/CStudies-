import numpy as np
import matplotlib.pyplot as plt

#There are fundamentally three types of function formaitons you can encounter at deriving a function:
# - addition of functions f+g -> d(fx+gx)/dx = d(fx)/dx + f(gx)/dx
# - product of functions f*g -> d(fx*gx)/dx = fx*d(gx)/dx + gx*d(fx)/dx 
# - composition of functions f o g ->d(f(gx))/dx = (d(f(gx))/dg)*(d(gx)/dx) [chain rule]
# Look at the chain rule. What d(f)/dg means is "how much f changes under a tiny change in g. "
# We multiply that ratio by "how much g changes under a tiny change in x."

# Helpful insigths on "chain rule video": When functions are being multiplied, it's helpful to 
# think of them as a product describing an area of a square, and the goal of the derivative is 
# figuring out how does the area of the square change under a tiny change in its sides.  

# Implicit differentiation is finding the derivative of an equation rather than a function, 
# which tells us how does a change in a variable affect the change in another variable 
# to keep the expression true:
# x**2 + y**2 = 5**2 -> 2x dx + 2y dy = 0 : for a point (x,y) and moving dx (or dy) by a tinny 
# amoun we can know the magnitude of dx (or dy), i.e. how much does x changes if y is changed 
# a bit from a point (x,y) 
# Other example: y = ln(x) -> e**y = x -> dy/dx -> e**y dy = dx (if we make a tinny step of dx
# from (x,y), how much does y change (i.e. what is the value of dy) ) --> dy/dx = 1/e**y
# So the slope of the graph y=ln(x) will have the value at any point y of 1/e**y or 
# at any point x will have a slope of 1/x 

def derivative(func, value):
	h = 1e-10
	return (func(value+h)-func(value))/h

def main(): 
	xaxis = np.arange(-2.5,2.5,1e-3)
	#basicDemo(xaxis)
	polynomials(xaxis)
	#exponentialsDemo(xaxis)

def basicDemo(xaxis):
	#graphs function and its derivative
	#func = lambda x: np.cos(x**2)
	func = lambda x: x/np.tan(x)
	dfunc = lambda x: (1/np.tan(x)) - (x/(np.sin(x)**2))
	
	funcVals = [func(i) for i in xaxis]
	dfuncVals = [derivative(func, i) for i in xaxis]
	dfuncVals2 = [dfunc(i)+1 for i in xaxis]
	plt.figure()
	plt.plot(xaxis, func(xaxis))
	#plt.plot(xaxis, dfuncVals)
	#plt.plot(xaxis, dfuncVals2)
	plt.show()

def polynomials(xaxis):
	from functools import reduce
	degree = 3
	fs_ = []
	for i in range(1,degree):
		fs_.append(lambda x: i*np.power(x,i))
	fs = lambda x: reduce(lambda i,j: i+j, [fs_[i](x) for i in range(len(fs_))]) # basically a polynomial a[0]*x**0 + a[1]*x**1 + ...		
	fsv = [fs(i) for i in xaxis]

	dfsv = [derivative(fs, x) for x in xaxis]

	plt.plot(xaxis, fsv)
	plt.plot(xaxis, dfsv)
	plt.show()


def exponentialsDemo(xaxis):
	# Visualization of exponentials and its derivative for different basis to 
	# gain intuition on the difference between its derivative and the function itself
	# (e**x -> d(e**x)/dx = e**x)
	# This is due to a property of exponents whereas their derivative is proportional to iself
	# and the constant is (base**h - 1)/h, whereas if base=e, this constant aproaches 1. 
	# For basis>e -> constant is >1 (hence making their derivative with slightly bigger values)
	# For basis<e -> constant is <1 (hence making their derivative with slightly smaller values)	 
	basis = [1,2, np.e, 3, np.pi, 4, 5, 6, 7, 8, 9, 10]

	for i in range(len(basis)):
		function = lambda x: basis[i]**x
		fvs = [function(x) for x in xaxis]
		dfvs = [derivative(function, x) for x in xaxis]
		plt.figure()
		plt.plot(xaxis, fvs)
		plt.plot(xaxis, dfvs)
		plt.title(f'base: {basis[i]}')
		plt.show()

	constantOfExpDerivatives(basis)

def constantOfExpDerivatives(basis):
	# Indeed, these constants have a certain special sense, and indeed they are the natural log of the basis: ln(b)
	# b**t = e**(ln(b)*t) -> d(b**t)/dt = d(e**(ln(b)*t))/dx = b**t * ln(b)
	dt = 1e-10
	constantFunc = lambda b: (b**dt - 1) / dt
	cfvs = [ constantFunc(base) for base in basis ]
	plt.figure()
	plt.plot(basis, cfvs)
	plt.title('Constants for exponential\'s derivatives as a function of their base')
	plt.show()


if __name__ == '__main__':
	main()