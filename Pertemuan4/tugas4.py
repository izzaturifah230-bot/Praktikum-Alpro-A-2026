#3

class NamaTidakValid(Exception) :
    def __init__ (self, nama):
        self.nama = nama
        super().__init__(f"nama harus mengandung at least 3 huruf ")

class EmailCacat(Exception) :
    def __init__ (self, email):
        self.email = email
        super().__init__(f"email harus mengandung '@'. ")

class NomorTidakValid(Exception) :
    def __init__ (self, nomor):
        self.nomor = nomor
        super().__init__(f"No HP tidak valid! Harus 10-13 digit angka.")

class UmurTidakMemenuhi(Exception):
    def __init__ (self, nomor):
        self.nomor = nomor
        super().__init__(f"Umur tidak memenuhi syarat (17-60 tahun).")



def cek_nama(nama):
        if len(nama) < 3 :
            raise NamaTidakValid(nama)
        return True
    
def cek_email(email):
        if '@' in email :
            pass
        else :
            raise EmailCacat(email)
        return True
    
def cek_umur(umur):
        if umur < 17 or umur > 60 :
            raise UmurTidakMemenuhi(umur)
        return True
    
def cek_nomor(nomor):
        if 10 <= len(nomor) <=13 :
            pass
        else : 
            raise NomorTidakValid(nomor)
        return True
            
print("=== REGISTRASI PESERTA SEMINAR ===")

try :
    while True :
        try :
            nama = input("Nama lengkap : ")
            namaValid = cek_nama(nama)
        except NamaTidakValid as e :
            print (F"[EROR] {e}" ) 
        else : 
            break

    while True :
        try :
            umur = int(input("Umur : "))
            umurValid = cek_umur(umur)
        except ValueError :
            print("masukkan bilangan bulat")
        except UmurTidakMemenuhi as e :
            print (F"[EROR] {e}" ) 
        else : 
            break

    while True :
        try :
            email = input("Email : ")
            emailValid = cek_email(email)
        except EmailCacat as e :
            print (F"[EROR] {e}" ) 
        else : 
            break

    while True :
        try :
            nomor = input("Nomor : ")
            nomorValid = cek_nomor(nomor)
        except NomorTidakValid as e :
            print (F"[EROR] {e}" ) 
        else : 
            break
finally :
    print("input berhasil")

print(f"""
=== DATA PESERTA ===
Nama    : {nama}
Umur    : {umur}
Email   : {email}
No HP   : {nomor}
Status  : TERDAFTAR
""")

print("selesai")