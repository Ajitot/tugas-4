import numpy as np

#soal no 1
A = np.array([[1, 2], [3, 4]])
#menghitung determinan matriks
determinant = np.linalg.det(A)

print('determinant matriks A:\n' , determinant)

#soal no 2
B = np.array([[10, -22], [3, 45]])
#menghitung invers matriks
inverse_of_B = np.linalg.inv(B)

print('invers matriks B:\n', inverse_of_B)

#soal no 3
C = np.array([[1, 10**-10], [10**-10, 1]])
#apakah matriks berkondisi buruk
from numpy.linalg import\
     cond
C = np.array([[1, 10**-10], [10**-10, 1]])

print('condition number:\n', cond(C))

#Soal No.4
from numpy.linalg import \
              matrix_rank
A = np.array([[1,2],
              [3,4]])
print('Rank:\n', matrix_rank(A))
b = np.array([[5], [6]])
A_b = np.concatenate((A, b), axis = 1)
print('Augmented matrix:\n', A_b)

#Soal No.5
# Tentukan matriks Anda (contoh matriks 3x3)
A = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# Hitung peringkat matriks
rank = np.linalg.matrix_rank(A)

# Hitung dimensi ruang nol
num_columns = A.shape[1]
nullity = num_columns - rank

# Cetak hasil
print("Matriks:")
print(A)
print("Peringkat Matriks:", rank)
print("Dimensi Ruang Nol:", nullity)