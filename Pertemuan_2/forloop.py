# Perulangan For Python
# Cetak setiap buah dalam daftar buah:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Bahkan string pun merupakan objek yang dapat diiterasi, karena berisi urutan karakter:

# Contoh
# Lakukan perulangan melalui huruf-huruf dalam kata "pisang":

# Keluar dari perulangan ketika x"pisang":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
# Cetak semua angka dari 0 hingga 5, dan cetak pesan ketika perulangan telah berakhir:

for x in range(6):
  print(x)
else:
  print("Finally finished!")

# Tuliskan setiap kata sifat untuk setiap buah:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
