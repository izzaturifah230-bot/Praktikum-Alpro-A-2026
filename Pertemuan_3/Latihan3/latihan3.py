class Univ:
  def __init__(self, nama, daerah, tahun, jumlahPopulasi):
    self.nama = nama
    self.daerah = daerah
    self.tahun = tahun
    self.jumlahPopulasi = jumlahPopulasi

  def perkenalan(self):
    print(f"nama univ : {self.nama}, berdiri dari tahun {self.tahun}")
  
  def ubahPopulasi(self, jumlahPopulasi):
    self.jumlahPopulasi = jumlahPopulasi
    

u1 = Univ("ITB", "nangor", "1920", 2000)
u2 = Univ("unri", "riau", "1900", 100)
u3 = Univ("ui", "depok", "2000", 13000)
print(u1.jumlahPopulasi)

print(type(u1))

aku = [1, 2, 3]
print(type(aku))