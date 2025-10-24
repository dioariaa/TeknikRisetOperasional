import numpy as np
from scipy.optimize import linprog

c = np.array([
    10, 7, 9, 11,
    12, 10, 8, 13,
    8, 11, 10, 9
])

A_ub = np.array([
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
])
b_ub = np.array([250, 200, 250])

A_eq = np.array([
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]
])
b_eq = np.array([150, 200, 100, 150])

result = linprog(c, 
                 A_ub=A_ub, b_ub=b_ub,
                 A_eq=A_eq, b_eq=b_eq,
                 method='highs')

if result.success:
    print(f"Status: Optimasi Berhasil!")
    print(f"Total Biaya Minimum: Rp {result.fun}")
    solution_matrix = result.x.reshape(3, 4)
    print("\nTabel Alokasi Optimal (Unit):")
    print(solution_matrix)
else:
    print("Solver gagal menemukan solusi.")