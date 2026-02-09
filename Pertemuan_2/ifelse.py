#Python If Statement

# Pernyataan if:
a = 33
b = 200
if b > a:
  print("b is greater than a")

# Memeriksa apakah suatu angka positif:
number = 15
if number > 0:
  print("The number is positive")

# menggunakan variabel boolean
is_logged_in = True
if is_logged_in:
  print("Welcome back!")

#elif
#  "jika kondisi sebelumnya tidak benar, maka coba kondisi ini"./
# Menguji berbagai kondisi:
score = 75
if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")

day = 3
if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")

#Else Python
#  dieksekusi ketika kondisi if (dan kondisi elif lainnya ) bernilai False .
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# Memeriksa bilangan genap atau ganjil:
number = 7
if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

#shorter than if
a = 5
b = 2
if a > b: print("a is greater than b")

# Satu baris if/ elseyang mencetak sebuah nilai:
a = 2
b = 330
print("A") if a > b else print("B")

a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

#nested if
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# Memeriksa beberapa kondisi dengan penestingan:
age = 25
has_license = True

if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")


# Tiga tingkatan penestingan:
score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")
