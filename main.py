# Triángulos adultos

# NOTE: In this version f's inputs are the parents and the grandparent.

def triangle(f, axioms = [[1], [1, 1]], border = 0, layers = 10):
    triangle = list(axioms)

    for i in range(len(triangle), layers + len(triangle) - 1):
        new_layer = []

        new_layer.append(f(border, triangle[i - 1][0], border))

        for j in range(0, len(triangle[i - 1]) - 1):
            left_parent = triangle[i - 1][j]
            right_parent = triangle[i - 1][j + 1]
            grandparent = triangle[i - 2][j]

            new_layer.append(f(left_parent, right_parent, grandparent))

        new_layer.append(f(triangle[i - 1][-1], border, border))

        triangle.append(new_layer)

    return triangle
