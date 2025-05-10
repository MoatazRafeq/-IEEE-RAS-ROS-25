import math

def vector_subtract(a, b):
    return [a[i] - b[i] for i in range(3)]

def dot_product(a, b):
    return sum(a[i] * b[i] for i in range(3))

def cross_product(a, b):
    return [
        a[1]*b[2] - a[2]*b[1],
        a[2]*b[0] - a[0]*b[2],
        a[0]*b[1] - a[1]*b[0]
    ]

def magnitude(v):
    return math.sqrt(sum(i**2 for i in v))

# Read input
points = [list(map(float, input().split())) for _ in range(4)]
A, B, C, D = points

# Calculate vectors
AB = vector_subtract(B, A)
AC = vector_subtract(C, A)
BC = vector_subtract(C, B)
BD = vector_subtract(D, B)

# Calculate normals
X = cross_product(AB, AC)
Y = cross_product(BC, BD)

# Calculate angle between normals
cos_theta = dot_product(X, Y) / (magnitude(X) * magnitude(Y))
angle = math.acos(cos_theta)

# Convert to degrees
angle_degrees = math.degrees(angle)

# Print result with two decimal places
print(f"{angle_degrees:.2f}")
