#The while Loop
#With the while loop we can execute a set of statements as long as a condition is true.
i = 1
while i < 6:
  print(i)
  i += 1

#continue
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#for  looping
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


