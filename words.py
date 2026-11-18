import numpy as np
def num_letters(num_rows, num_columns):
    return num_rows*num_columns-(num_rows-2)*(num_columns-2)
assert num_letters(3, 4) == 10  #3 is the num_rows and 4 is the num_columns
print("Checking assertions.")
data = np.loadtxt("loop2.csv", delimiter=",", dtype=str, encoding = 'utf8')
words = [] #this will store the letters we extract from the data file
rows, columns = data.shape  #this gives you the number of rows and number of columns in the data file
#collect all letters - fill in your code here
assert num_letters(4,4) == 12 #loop2
assert num_letters(13,4) == 30 #loop1
assert num_letters(6,4) == 16 #loop3
assert num_letters(6,7) == 22 #loop4
