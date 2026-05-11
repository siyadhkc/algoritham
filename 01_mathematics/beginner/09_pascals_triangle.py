def pascal_triangle(n):
    triangle = []

    for row in range(n):
        current_row = [1] * (row + 1)

        for col in range(1, row):
            current_row[col] = (
                triangle[row - 1][col - 1] +
                triangle[row - 1][col]
            )

        triangle.append(current_row)

    return triangle


# Input
n = int(input("Enter number of rows: "))

triangle = pascal_triangle(n)

# Print triangle
for row in triangle:
    print(row)