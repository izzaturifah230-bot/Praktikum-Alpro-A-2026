#list

# Akses Item
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thatlist = [1,"dua",3]
print(thatlist)

# Cetak item terakhir dari daftar:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Kembalikan item ketiga, keempat, dan kelima:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#index
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#split
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#check if item exist
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[0:4] = ["blackcurrant", "watermelon"]
print(thislist)

#Remove Specified Item

#by value
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#by index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#remove entire

