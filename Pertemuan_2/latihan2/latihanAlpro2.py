#1
def fizzbuzz_plus(n:int):
    a = int(n)
    for i in range(1, a+1):
        if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz") 
        elif i % 3 == 0 :
            print("Fizz") 
        elif i % 5 == 0 :
            print("buzz") 
        elif i % 7 == 0 :
            print("seven") 
        else :
            print(i)

angka = input("masukkan banyak angka :")
print(fizzbuzz_plus(angka))

#2
def hitung_nilai(tugas:int, uts:int, uas:int):
    a = tugas *0.30
    b = uts *0.30
    c = uas *0.40
    nilai = a + b + c
    print(f"nilai : {nilai}")
    if nilai >= 85 :
        print("grade : A")
    elif 70 <= nilai <85 :
        print("grade : B")
    elif 55 <= nilai <70 :
        print("grade : C")
    elif 40 <= nilai <55 :
        print("grade : D")
    else :
        print("grade : E")

tugas = int(input("masukkan nilai tugas:"))
uts = int(input("masukkan nilai uts:"))
uas = int(input("masukkan nilai uts:"))

print(hitung_nilai(tugas,uts,uas))

#3
def is_password_valid(password):
    nilaipw = 0

    if len(password) >= 8:
        nilaipw += 1
    
    if " " in password :
        nilaipw += 1

pw = input("masukkan pw:")    

print(is_password_valid(pw))
    




    