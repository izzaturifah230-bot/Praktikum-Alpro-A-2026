# 1
data = ["10", "20", "30"]
try :
    idx = int(input("masukan index (0-2) : "))
    print(f"hasil 3 = {data[idx]}")
except IndexError :
    print("nggak sesuai jangkauan")
except ValueError :
    print("masukkan angka, jangan huruf")
finally :
    print("selesaiii!!!")

#2
try :
    pembilang = float(input("maukkan angka yang akan dibagi : "))
    penyebut = float(input("masukkan angka pembagi : "))
    print(f"hasil bagi = { pembilang / penyebut}")
except ValueError : 
    print("masukkan bilangan real ")
except ZeroDivisionError :
    print("penyebut nggak boleh 0")
finally :
    print("program berhasil")
