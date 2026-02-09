# Tuple digunakan untuk menyimpan beberapa item dalam satu variabel.

thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tidak dapat diubah

# Izinkan Duplikat
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Panjang Tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# Mengakses Item Tuple
# Cetak item kedua dalam tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Cetak item terakhir dari tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# Kembalikan item ketiga, keempat, dan kelima:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# Periksa apakah "apel" ada dalam tuple:

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# Memperbarui Tuple
# Ubah tuple menjadi list agar bisa diubah:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Ubah tuple menjadi list, tambahkan "orange", lalu ubah kembali menjadi tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# Gabungkan Dua Tuple
# Gabungkan dua tuple:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Kalikan pasangan buah-buahan tersebut dengan 2:

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
