# Create an array of the form  b=[12]b=[12] 

import numpy as np
b = np.array([[1],[2]])
print(b)

# Create a 2x2 array of the form  X=[1324]X=[1234] 
x = np.array([[1,2],[3,4]])
print(x)

# Multiply the two arrays element wise, then using matrix multiplication, 
# and finally the inner product of  b∙bb∙b .

# element wise multiplication

elem_mult = np.multiply(b,x)
print(elem_mult)

matrix_mult = b*x
print(matrix_mult)

dot_mult = np.dot(x,b)
print(dot_mult)

# For each of your results in part (3), print the shape and data type.

print([[elem_mult.shape, elem_mult.dtype]])

# Reshape (or flatten), the array  X  such that it consists of only 1 row.

x.flatten()

# Create an array of the integers 1 to 10, inclusive, setting the datatype to 
# float.

ar = np.arange(10)

float_array = ar.astype(np.float)

# Create a 10x10 identity matrix using the built in numpy function.

np.identity(10)

# Create a 10x10 identity matrix using a for loop.

mat = []

dim = int(input(10))

for i in range(0,dim):
    row = []
    mat.append(row)
    
    for j in range(0, dim):
        if i == j:
            row.append(1)
        else: row.append(0)
        
        print(mat)
        
        
matrix = [[1 if i == j else 0 for i in range(dimension)] for j in range(dimension)]
matrix        
            

# Generate a set of random data,  X , drawn from a normal distribution, 
# consisting of 9 columns of 100 rows each, then attach a column of all ones, 
# resulting in a 100x10 matrix for  X . 
#Next generate a random array  ββ , drawn from a uniform distribution, of length 10. Also make an array,  ϵϵ  of length 100, drawn from a normal distribution. Finally, compute a vector  y⃗ y→ such that  y⃗ =Xβ+ϵy→=Xβ+ϵ . Be sure to set the random seed to 0 before drawing any random numbers. All random numbers should be on the interval [0, 1).
Using the vector  y⃗ y→  computed in part 9, create a vector  c⃗ c→  containing the labels "positive" or "negative" for each value in  y⃗ y→ , treating 0 as positive. Bonus: Do it with a one-liner.
Using the classes generated in part 10, separate the matrix X into two smaller matricies,  XpXp ,  XnXn , containing only rows which map to positive or negative values respectively.
Generate a meshgrid on the interval [0, 1], of shape 100x100. Then compute the Euclidean Distance given by  d=x2+y2⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯√d=x2+y2  from the origin for each unit,  (xn,yn)(xn,yn) , in the grid. Bonus: Do it with a one-liner.
Generate a set of 100 values,  pp , on the interval  [0,2π][0,2π]  and two vectors,  x⃗ ,y⃗ x→,y→  such that  x⃗ =cos(p)x→=cos(p)  and  y⃗ =sin(p)y→=sin(p) . Then compute the vector  r⃗ =x2+y2⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯√r→=x2+y2 . Comment on your results.
Generate two lists, a, b, consisting of 10 randomly drawn values from a normal and uniform distribution respectively. Compute the mean and median of each.
Using a from part 14, create a new list c by calling a = c. Now change the shape of c. Comment on your results.
How would you solve the problem that appeared in part 15?