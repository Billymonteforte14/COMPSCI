import numpy as np

five_by_five = np.arange(1, 26).reshape(5, 5)
third_row = five_by_five[2]
last_two_columns = five_by_five[:, -2:]
center_submatrix = five_by_five[1:4, 1:4]
print("5x5 Matrix:")
print(five_by_five)
print("Third Row:")
print(third_row)
print("Last Two Columns:")
print(last_two_columns)
print("3x3 Center Submatrix:")
print(center_submatrix)
