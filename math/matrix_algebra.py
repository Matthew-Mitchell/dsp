# Matrix Algebra
A=np.array([[1,2,3],[2,7,4]])
B=np.array([[1,-1],[0,1]])
C=np.array([[5,-1],[9,1],[6,0]])
D=np.array([[3,-2,-1],[1,2,3]])
u=np.array([[6,2,-3,5]])
v=np.array([[3,5,-1,4]])
w=np.array([[1],[8],[0],[5]])
print "Question 1:\n"
dimensions=[x.shape for x in [A,B,C,D,u,w]]
for dim in dimensions:
    print "1."+str(dimensions.index(dim)+1)+")", dim
print "\nQuestion 2:\n"
def dot(x,y):
    try:
        return np.dot(x,y)
    except:
        return "Not defined."
alpha=6
print "2.1)", u+v
print "2.2)", u-v
print "2.3)", alpha*u
print "2.4)", dot(u,v)
print "2.5)", np.linalg.norm(u)

print"\nQuestion 3:\n"
print "3.1)", "Not defined"
print "3.2)\n", A-np.transpose(C) 
print "3.3)\n", np.transpose(C)+3*D
print "3.4)\n", dot(B,A)
print "3.5)\n", dot(A,B)

print"\nOptional Extensions\n"
print "3.6)\n", dot(B,C)
print "3.7)\n", dot(C,B)
print "3.8)\n", np.linalg.matrix_power(B,4)
print "3.9)\n", dot(A,np.transpose(A))
print "3.10)\n", dot(np.transpose(D),D)
