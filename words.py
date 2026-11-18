import numpy as np
def num_letters(num_rows, num_columns):
    return num_rows*num_columns-(num_rows-2)*(num_columns-2)
assert num_letters(3, 4) == 10  #3 is the num_rows and 4 is the num_columns
assert num_letters(4,4) == 12 #loop2
assert num_letters(13,4) == 30 #loop1
assert num_letters(6,4) == 16 #loop3
assert num_letters(6,7) == 22 #loop4
print("Checking assertions.")
data = np.loadtxt("loop4.csv", delimiter=",", dtype=str, encoding = 'utf8')
words = [] #this will store the letters we extract from the data file
rows, columns = data.shape  #this gives you the number of rows and number of columns in the data file
#collect all letters - fill in your code here
for c in range(n_columns):
    words.append(data[

    
print(words) #check that you collected all the letters in your data file

assert len(words) == num_letters(rows, columns) 

  #this should not throw an error. If it does, most likely your main code is not getting the correct number of letters
