import numpy as np
import pandas as pd

# Question 6: Write a program to access the elements at
# 3rd column and 2nd row
# 3rd row
# 4th column
matrix = np.array([[1,2,3,4,5,6],
                  [7,8,9,10,11,12],
                  [13,14,15,16,17,18],
                  [19,20,21,22,23,24]])
print('Part 1 ->',matrix[1,2])
print('Part 2 ->',matrix[2,:])
print('Part 3 ->',matrix[:,3])

# Question 7: Write aprogram to convert a matrix to a 1 D array

print('Shape of 2D Matrix Before ->',matrix.shape)
matrix = matrix.reshape(matrix.shape[0] *matrix.shape[1])
print('Converted Matrix ->',matrix)
print('Shape of Converted Matrix',matrix.shape)

# Question 8: Write a program to create an empty data frame

df = pd.DataFrame()
print(df)

# Question 9: Write a program to create a data frame from 4 given vectors

v1 = ['Shreshth','20','Indian','0 Years']
v2 = ['Bastista','30','American','5 Years']
v3 = ['John','35','American','10 Years']
v4 = ['Rock','45','American','15 Years']

print('4 given Vectors are :')
print('1 ->',v1)
print('2 ->',v2)
print('3 ->',v3)
print('4 ->',v4)
df = pd.DataFrame([v1,v2,v3,v4], columns = ['Name',
                                            'Age',
                                            'Nationality',
                                           'Experience'],
                 index=[1,2,3,4])
print('The data frame is:')
print(df);

# Question 10: Write a program to get the structure of a data frame

print(df.describe)