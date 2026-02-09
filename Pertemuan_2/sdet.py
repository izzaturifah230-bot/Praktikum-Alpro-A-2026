# Set Item

# Nilai duplikat akan diabaikan:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# True dan 1dianggap memiliki nilai yang sama:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# Himpunan yang berisi nilai string, bilangan bulat, dan boolean:
set1 = {"abc", 34, True, 40, "male"}

# Akses Item
# Lakukan perulangan melalui himpunan tersebut, dan cetak nilainya
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

# Contoh
# Periksa apakah "pisang" ada dalam himpunan tersebut:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# Contoh
# Periksa apakah "pisang" TIDAK ada dalam himpunan:
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)

# Gabungkan Set
# Gabungkan set1 dan set2 menjadi set baru:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# Digunakan |untuk menggabungkan dua himpunan:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

# Gabungkan beberapa himpunan dengan union()metode:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)

# Gabungkan himpunan dengan tuple:
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

# Metode ini update()memasukkan item-item dalam set2 ke dalam set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# Python frozenset
# frozensetadalah versi himpunan yang tidak dapat diubah.

# Buat sebuah objek frozensetdan periksa tipenya:
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
