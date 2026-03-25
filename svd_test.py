import numpy as np

toy_matrix = np.array([
    [5.0, 4.0, 0.0, 1.0],
    [4.0, 5.0, 0.0, 1.0],
    [1.0, 1.0, 0.0, 5.0],
    [0.0, 0.0, 5.0, 4.0],
    [0.0, 0.0, 4.0, 5.0],
])

U, s, Vt = np.linalg.svd(toy_matrix, full_matrices=False)

print("U  shape:", U.shape)
print("s  shape:", s.shape)
print("Vt shape:", Vt.shape)
print()
print("Valores singulares:", s.round(4))
print("Rango de la matriz:", np.linalg.matrix_rank(toy_matrix))
