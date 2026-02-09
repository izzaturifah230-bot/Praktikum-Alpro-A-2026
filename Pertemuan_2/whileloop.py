# Cetak i selama i kurang dari 6:

i = 1
while i < 6:
  print(i)
  i += 1

# Pernyataan jeda
# Dengan pernyataan break , kita dapat menghentikan perulangan meskipun kondisi while benar:

# Contoh
# Keluar dari loop ketika i adalah 3:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# Pernyataan lanjutan
# Dengan pernyataan continue, kita dapat menghentikan iterasi saat ini, dan melanjutkan ke iterasi berikutnya:

# Contoh
# Lanjutkan ke iterasi berikutnya jika i adalah 3:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# Pernyataan else
# Dengan pernyataan else , kita dapat menjalankan blok kode sekali saja ketika kondisi tersebut tidak lagi benar:

# Contoh
# Cetak pesan setelah kondisinya salah:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
