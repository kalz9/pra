import numpy as np

# Union of fuzzy sets
def fuzzy_union(A, B):
    return np.maximum(A, B)

# Intersection of fuzzy sets
def fuzzy_intersection(A, B):
    return np.minimum(A, B)

# Complement of a fuzzy set
def fuzzy_complement(A):
    return 1 - A

# Difference of fuzzy sets
def fuzzy_difference(A, B):
    return np.maximum(A - B, 0)

# Fuzzy relation by Cartesian product
def fuzzy_cartesian_product(A, B):
    R1 = []
    for i in range(len(A)):
        for j in range(len(B)):
            R1.append([A[i], B[j]])
    return np.array(R1)

# Max-Min Composition of fuzzy relations
def max_min_composition(R1, R2):
    R3 = np.zeros((len(R1), len(R2)))
    for i in range(len(R1)):
        for j in range(len(R2)):
            R3[i][j] = np.max(np.minimum(R1[i], R2[j]))
    return R3


# User input for fuzzy sets A and B
A, B = [], []
n = int(input('Enter the number of values in the fuzzy set:'))
for i in range(n):
    A.append(float(input(f'Enter value {i+1} for fuzzy set A:')))
    B.append(float(input(f'Enter value {i+1} for fuzzy set B:')))

A = np.array(A)
B = np.array(B)

# Test the operations
print("Union:", fuzzy_union(A, B))
print("Intersection:", fuzzy_intersection(A, B))
print("Complement of A:", fuzzy_complement(A))
print("Difference of A and B:", fuzzy_difference(A, B))

# Fuzzy relations by Cartesian product
R1 = fuzzy_cartesian_product(A, B)
R2 = fuzzy_cartesian_product(B, A)
print("Fuzzy relation R1:", R1)
print("Fuzzy relation R2:", R2)

print(np.max(np.minimum(R1[0], R2[0])))

# Max-Min Composition of fuzzy relations
R3 = max_min_composition(R1, R2)
print("Max-Min Composition R3:", R3)