#1. Import the NUMPY package under the name np.

import numpy as np

#2. Print the NUMPY version and the configuration.

print(np.__version__)
np.show_config()

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

Dos elementos matriciales de 3 filas con 5 columnas

a=np.random.random(2,3,5)

#4. Print a.

print(a)


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b=np.ones((5,2,3))

#6. Print b.

print(b)


#7. Do a and b have the same size? How do you prove that in Python code?


print(a.shape==b.shape)

Imprimira False


#8. Are you able to add a and b? Why or why not?

No, porque su tamaño no es el mismo(ValueError: operands could not be broadcast together with shapes (2,3,5) (5,2,3))

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c=b.T

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

c=np.reshape(c(2,3,5))
d=np.add(a,c)

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print(a,"\n\n\n",d)


#12. Multiply a and c. Assign the result to e.

e=np.multiply(a,c)
print(e)

#13. Does e equal to a? Why or why not?

'e' es igual a 'a' porque c es una matriz de unos, multiplicando elemento a elemento, los elementos de 'a' son multiplicados por los elementos (unos) de 'e'


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"


d_max=d.max()
d_min=d.min()
d_mean=d.mean()

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.


f=np.empty((2,3,5))

"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""
import numpy as np
a = np.random.random((2, 3, 5))
print("a=\n", a)
c = np.ones((2, 3, 5))
print("c=\n", c)
d = np.add(a, c)
d_min = d.min()
d_max = d.max()
d_mean = d.mean()
f = np.empty((2,3,5))
print("\nd_min= ", d_min, "\nd_max= ", d_max, "\nd_mean=", d_mean)
print("d=\n", d)
for i in range(len(f)):
    for j in range(len(f[i])):
        for k in range(len(f[i][j])):
            if d_min < d[i][j][k] < d_mean:
                f[i][j][k] = 25
            if d_mean < d[i][j][k] < d_max:
                f[i][j][k] = 75
            if d[i][j][k]==d_mean:
                f[i][j][k] = 50
            if d[i][j][k]==d_min:
                f[i][j][k] = 0
            if d[i][j][k]==d_max:
                f[i][j][k] = 100
print("f=\n", f)       




"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""

d=
 [[[1.20887273 1.50360296 1.24181221 1.55603971 1.37235487]
  [1.6311726  1.90235462 1.20033319 1.757012   1.2062956 ]
  [1.79851723 1.59980883 1.18526149 1.01394988 1.98837796]]

 [[1.98610685 1.43225584 1.07400598 1.77271156 1.67084631]
  [1.83293063 1.56041544 1.09131267 1.60067241 1.13088824]
  [1.05912111 1.69765943 1.30315866 1.68011554 1.82248679]]]
f=
 [[[ 25.  75.  25.  75.  25.]
  [ 75.  75.  25.  75.  25.]
  [ 75.  75.  25.   0. 100.]]

 [[ 75.  25.  25.  75.  75.]
  [ 75.  75.  25.  75.  25.]
  [ 25.  75.  25.  75.  75.]]]



"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""

import numpy as np
a = np.random.random((2, 3, 5))
print("a=\n", a)
c = np.ones((2, 3, 5))
print("c=\n", c)
d = np.add(a, c)
d_min = d.min()
d_max = d.max()
d_mean = d.mean()
f = np.ones((2,3,5))
print("\nd_min= ", d_min, "\nd_max= ", d_max, "\nd_mean=", d_mean)
for i in range(len(f)):
    for j in range(len(f[i])):
        for k in range(len(f[i][j])):
            if d_min < d[i][j][k] < d_mean:
                f[i][j][k] = "B"
            if d_mean < d[i][j][k] < d_max:
                f[i][j][k] = "D"
            if d[i][j][k]==d_mean:
                f[i][j][k] = "C"
            if d[i][j][k]==d_min:
                f[i][j][k] = "A"
            if d[i][j][k]==d_max:
                f[i][j][k] = "E"
print("d=\n", d)
print("f=\n", f)

