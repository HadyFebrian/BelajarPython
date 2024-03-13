#Penerapan
matriks = [[1,2,3],
           [4,5,6],
           [7,8,9]]
print(matriks)
#Menggunakan Library Numpy
import numpy
matriks = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print(matriks)
#Perbandingan Memori Menggunakan Matriks Python dan Numpy
import numpy
import sys
var_list= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
var_array= numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])
print("Ukuran keseluruhan elemen list dalam bytes = ",sys.getsizeof(var_list)*len(var_list))
print("Ukuran keseluruhan elemen NumPy dalam bytes = ", var_array.size*var_array.itemsize)
#Deklarasi Matriks
#Deklarasi Sekaligus Inisiasi Nilai Matriks
matriks = [[1,2,3],
           [4,5,6],
           [7,8,9]]
print(matriks)
#Deklarasi Default Nilai Matriks
matriks =[[0 for i in range(3)]for j in range(3)]
print(matriks)
#Akses Element Matriks
var_mat = [[1, 2, 3, 4, 5],
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]]
print(var_mat[2][1])
#Operasi Aritmatika
#Deklarasi Variabel
var_mat = [[5,4],
           [6,2]]
#Deklarasi Variabel Default
def_mat = [[0 for i in range(2)]for j in range(2)]
#Melakukan Perulangan
for i in range(len(var_mat)):
  for j in range(len(var_mat[0])):
      #Melakukan Proses Perkalian Dengan Matriks (2)
      def_mat[i][j] = var_mat[i][j] * 2
print(def_mat)
#Mencoba Menggunakan Library Numpy
#Deklarasi Nilai Default
import numpy
matriks=numpy.array([[0 for i in range(5)]for j in range(5)])
print(matriks)
#Operasi Aritmatika
var_mat = numpy.array([[5,4],[6,2]])
hasil = var_mat * 2
print(hasil)