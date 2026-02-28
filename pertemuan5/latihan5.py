
A = [[5, 3, 1],
     [2, 8, 4],
     [6, 0, 7]]

B = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

# a
print("\nsoal no 1 : penambahan A dan B")
def tambah_matriks(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print('Error: ukuran matriks tidak sama')
        return None
    baris, kolom = len(A), len(A[0])
    hasil = [[A[i][j] + B[i][j] for j in range(kolom)] for i in range(baris)]
    return hasil



c_tambah = tambah_matriks(A, B)
for i in c_tambah :
    print(i)

# b
print("\nsoal no 2 pengurangan A dan B")
def kurangi_matriks(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print('Error: ukuran matriks tidak sama')
        return None
    baris, kolom = len(A), len(A[0])
    hasil = [[A[i][j] - B[i][j] for j in range(kolom)] for i in range(baris)]
    return hasil

c_kurang = kurangi_matriks(A, B)
for i in c_kurang :
    print(i)

# c
print("\nsoal no 3 : perkalian A dengan 4 ")
def kali_skalar(matriks, k):
    hasil = []
    for baris in matriks:
        baris_baru = [elemen * k for elemen in baris]
        hasil.append(baris_baru)
    return hasil

c_skalar = kali_skalar(A, 4)
for i in c_skalar:
    print(i)
