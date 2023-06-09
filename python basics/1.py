#Matrices

# matrix=[[1,2,3],[3,4,5],[5,6,7]]

# print("Matrix= ",matrix)

# Function to input a matrix from the user
def input_matrix(rows, columns):
    matrix = []
    print("Enter the elements of the matrix:")
    for i in range(rows):
        row = []
        for j in range(columns):
            element = int(input(f"Enter element at position ({i+1},{j+1}): "))
            row.append(element)
        matrix.append(row)
    return matrix

# Function to display the matrix
def display_matrix(matrix):
    print("Matrix:")
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

# Get the dimensions of the matrix from the user
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

# Input the matrix
matrix = input_matrix(rows, columns)

# Display the matrix
display_matrix(matrix)


