# Rotate Matrix
# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees.
# Can you do this in place?

# Current Solution
# Time Complexity: O(n^2) where n is the side length of the matrix
# Space Complexity: O(1) because we are rotating in place.

def rotate(matrix):
    print()
    for row in range(len(matrix)):
        for column in range(row):
            temp = matrix[row][column]
            matrix[row][column] = matrix[column][row]
            matrix[column][row] = temp
    for row in matrix:
        row.reverse()
    return matrix


print(rotate([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]))
