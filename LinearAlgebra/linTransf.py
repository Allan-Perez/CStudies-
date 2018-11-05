import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# A transformation is linear if it follows the following properties:
# Additivity: L(u+w) = L(u)+L(w)
# Scaling:    L(cv) = cL(v)
# Example of linear transformations to functions: derivative: chain rule. 
# Stuff worthy to note: Linear algebra concepts have direct connection to other fancy terminology 
# of utilities on other math fields that do the same at an underlying level: they are analog. 
# Linear transformations -> Linear operators
# Dot products -> Inner products
# Eigenvectors -> eigenfunctions 

#Other worhty notes -- 8 axioms that defines a vector space: 
# 1. u + (v + w) = (u + v) + w
# 2. u + w = w + u
# 3. 0 + v = v ; for every v
# 4. v + (-v) = 0; for every v
# 5. a(bv) = (ab)v
# 6. 1*v = v
# 7. a*(u + v) = au + av
# 8. (a + b)v = av + bv


def transform(vectors, transformation):
	assert transformation.shape[-1] == vectors.T.shape[0]
	V2 = np.dot(transformation, vectors.T).T
	return V2

def main():
	#demo2D()
	#demo3D()
	#demoBetweenDim()
	#basisChange()
	eigenstuff()

def demo2D():
	# V vector : V[0] = i_hat, V[1] = j_hat, V[2] = given vector
	origin = [0], [0]
	V1 = np.array([[1,0], [0,1], [1,2]])
	transf1 = np.array([[0,-1], [1,0]]) # π/2 rotation
	V2 = transform(V1, transf1)
	transf2 = np.array([[1,1],[0,1]]) # Shear
	V3 = transform(V2, transf2)
	transf3 = np.array([[1,-1], [1,0]]) # π/2 + shear hardcoded
	V4 = transform(V1, transf3)
	compositionTransf = np.dot(transf2, transf1) # π/2 + shear composite
	inverseComposite = np.dot(transf1, transf2) # shear + π/2 composite
	V5 = transform(V1, compositionTransf)
	V6 = transform(V1, inverseComposite)

	plt.quiver(*origin, V5[:,0], V5[:,1], angles='xy', scale_units='xy', scale=1)
	plt.quiver(*origin, V6[:,0], V6[:,1], color=['r','g','b'], angles='xy', scale_units='xy', scale=1)
	plt.grid(True)
	plt.xlim(-5,5)
	plt.ylim(-5,5)
	plt.show()

def demo3D():
	origin = [0],[0],[0]
	V1 = np.array([ [1, 0, 0], #i
					[0, 1, 0], #j
                	[0, 0, 1], #k
                	[1, 1, 1]])#v
	n_vectors = V1.shape[0]
	transform1 = np.array([[0,0,1],[0,1,0],[-1,0,0]]) # π/2 rotation on i_hat
	transform2 = np.array([[0,1,2],[3,4,5],[6,7,8]]) # shearing i
	transform3 = np.array([[0,-2,2],[5,1,5],[1,4,-1]]) # shearing k
	compostieTransf = np.dot(transform3, transform2)
	print(f'{compostieTransf}')
	U, V, W = zip(*V1)
	Ut, Vt, Wt = zip(*transform(V1, compostieTransf))
	oi, oj, ok = origin 
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.quiver(oi*n_vectors, oj*n_vectors, ok*n_vectors, U, V, W)
	ax.quiver(oi*n_vectors, oj*n_vectors, ok*n_vectors, Ut, Vt, Wt, color=['g','r','b'])
	ax.set_xlim([-2, 2])
	ax.set_ylim([-2, 2])
	ax.set_zlim([-2, 2])
	plt.show()

def demoBetweenDim():
	#_2dTo3d()
	_3dTo2d()

def _2dTo3d():
	# Basically with non-square matrices.
	origin = [0],[0],[0]
	V1 = np.array([ [1, 0], #i
					[0, 1], #j
                	[1, 1]])#v
	n_vectors = V1.shape[0]
	transf2Dto3D = np.array([[2,0],[-1,1],[-2,1]])

	U, V= zip(*V1)
	Ut, Vt, Wt = zip(*transform(V1, transf2Dto3D))
	oi, oj, ok = origin 
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	#ax.quiver(oi*n_vectors, oj*n_vectors, ok*n_vectors, U, V)
	ax.quiver(oi*n_vectors, oj*n_vectors, ok*n_vectors, Ut, Vt, Wt, color=['g','r','b'])
	ax.set_xlim([-2, 2])
	ax.set_ylim([-2, 2])
	ax.set_zlim([-2, 2])
	plt.show()

def _3dTo2d():
	# Basically with non-square matrices.
	origin = [0],[0]
	V1 = np.array([ [1,0,0], #i
					[0,1,0], #j
					[0,0,1], #k
                	[1,1,1]])#v
	n_vectors = V1.shape[0]
	transf3Dto2D = np.array([[3,1,4],[1,5,9]])

	Ut, Vt = zip(*transform(V1, transf3Dto2D))
	oi, oj = origin 
	#ax.quiver(oi*n_vectors, oj*n_vectors, ok*n_vectors, U, V)
	plt.quiver(oi*n_vectors, oj*n_vectors, Ut, Vt, color=['g','r','b', 'black'], angles='xy', scale_units='xy', scale=1)
	plt.grid(True)
	plt.xlim(-5,5)
	plt.ylim(-5,5)
	plt.show()


def basisChange():
	#Goal: to translate v from our basis to V1's basis (2,3)+(1,2)
	origin = [0],[0]
	V0 = np.array([ [1,0], #i
					[0,1], #j
                	[1,1]])#v

	V1 = np.array([ [2,3],
					[1,2]])
	n_vectors = V0.shape[0]
	translation = np.array([[2,3],[1,2]])
	noitalsnart = np.linalg.inv(translation)

	tV0 = transform(V0, noitalsnart)
	V1 = np.vstack((V1,tV0[-1]))

	oi, oj = origin 

	plt.quiver(oi*n_vectors, oj*n_vectors, V0[:,0], V0[:,1], angles='xy', scale_units='xy', scale=1)
	plt.quiver(oi*n_vectors, oj*n_vectors, V1[:,0], V1[:,1], color=['g','r','b'], angles='xy', scale_units='xy', scale=1)
	plt.grid(True)
	plt.xlim(-5,5)
	plt.ylim(-5,5)
	plt.show()


def eigenstuff():
	#Eigenvectors --> vectors that after a linear transformation, they're just stretched -- keeping their span unchanged, 
	#i.e. that a linear transformation or vector-matrix multiplication has the same effects as multiplying by a scalar.
	#Eigenvalue --> the factor by which the eigenvectors is stretched or squished during the transformation.
	# This can also be helpful to describe a 3D rotation in terms of an angle and an "axis" than a 3x3 matrix. 
	# Av = lv -> v is the eigenvector / l is the eigenvalue / A is the transformation matrix.
	# A = [[l,0,0],[0,l,0],[0,0,l]] -> Av = (lI)v | I is the identity matrix 
	# Goal: to solve for l and v.
	# Av - (lI)v = 0 -> (A-lI)v=0 --> This is going to be true always for v = zero vector, but also for other vectors.
	# Now, if v is nonzero, then the resulting matrix (A-lI) has to be a transformation that squishes space into lower dims, 
	# i.e. det(A-lI) = 0. 
	# For example, for a given linear transformation A = [[2,2],[1,3]], the only way det(A-lI)=0 is if l=1, meaning that when l=1
	# the transformation squishes space into lower dimension (in this case 1D), and that there exists a vector that when transformed, 
	# it equals the zero vector. This means that the vector v is an eigenvector of A (staying in its own span during the transformation A):
	# [[2,2],[1,3]]*v = 1*v
	# To find the corresponding eigenvectors, just go to the equation and solve: 
	# [[2-1, 2], [1,3-1]]*v = 0 -> [[1,2],[1,2]]*v = 0 -> so v is any vector on the span of (2,1) [i.e. (4,2),(6,3),...]
	# Even though,... a 2D matrix doesn't have to have eigenvectors (e.g. π/2 rotaiton). Some solutions on eigenvectors of π/2 rotations 
	# can end up with l=i and l=-i, the imaginary plane.
	# Another example: "SHEAR", A=[[1,1],[0,1]] -> l=1, meaning that the transformation's eigenvalue doesn't stretch the eigenvector.

	# Eigenbases-> after the transformation, the original basis (may be i and j) is just stretched or scaled by an eigenvalues.
	# These kind of transformation matrices have a particular shape: diagonal matrices, which have the particularity that all the 
	# base vectors are eigenvectors (i.e. after the transformation they are only scaled by a scalar) so that each entry of the diagonal matrix
	# is their corresponding eigenvalues. 

	# Note that if we have many eigenvectors for a given transformation (enough to keep the same rank), we may want to change our basis vectors 
	# (throw i and j, and get i' and j') so that our basis vectors become eigenbasis so that the transformation matrix A is just a diagonal matrix
	# with which may be far easier to work with. 
	# So if we want to do a transformation A=[[3,1],[0,2]] with eigenvectors v1= [1,0] and v2=[-1,1] (change basis transformation 
	# V=[[1,-1],[0,1]]), then we can change the basis with the "emphaty formula" V^-1 * A * V = A', where A' is a diagonal matrix which 
	# represents the original transformation in terms of stretching the eigenvectors. 

	# But note that not all transformations have eigenbasis, for example "shear", which only has 1 eigenvector (not enough for a basis).

	A = np.array([[0,1],[1,1]])
	B = A
	for n in range(1,10):
		B = np.dot(A,B)
	print(f"A^10:{B}")

	eigenvector1 = np.array([2,1+np.sqrt(5)])
	eigenvector2 = np.array([2,1-np.sqrt(5)])

	eigenbasis = np.vstack((eigenvector1, eigenvector2)).T
	
	diagmat = np.dot(np.linalg.inv(eigenbasis), np.dot(A, eigenbasis)).round(5)**10
	invertedDiag = np.dot(eigenbasis, np.dot(diagmat,np.linalg.inv(eigenbasis))).round(5)

	print(f'{A}')
	print(f'{diagmat}')
	print(f'{invertedDiag}')

if __name__ == '__main__':
	main()