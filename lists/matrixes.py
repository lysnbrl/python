"""In Python, we can create matrixes using lists, we just need to make a list that contains other 
lists; by n number of lists, we can create n-dimensional matrixes"""
row_a = [10, 20, 30]
row_b = [40, 50, 60]

matrix = [row_a, row_b]
print(matrix)

"""To obtain an item of a matrix, we need to place the x-position and the y-position of the item 
we want to obtain between the square brackets of the matrix"""
#This one will give us the first item
print(matrix[0][0])
#This one will give us the last item
print(matrix[1][2])
