#1
import random
dices = []
n = int(input("How many dice to roll:"))
i = 1
sum = 0
while n > 0:
    dice = random.randint(1,6)
    dices.append(dice)
    n = n - 1
print(dices)
for dice in dices:
    sum = sum + dice
print(sum)

#2
num = float(input("Enter a number:"))
nums = []
while str(num) != " ":
    nums.append(num)
    num = input("Enter a number:")
    if str(num) == " ":
      nums.sort(reverse = True)
      print(nums[:5])
      break
    else:
      num = float(num)


#3
n = int(input("Enter an integer:"))
List = []
for i in range(2,n):
 List.append(i)
 if n%i == 0:
   print("The number is NOT a prime number")
   break
else:
  print("The number is a prime number")

#4
cities = []
city = str(input("Enter the names of five cities one by one:"))
cities.append(city)
for i in range(0,4):
  item = str(input())
  cities.append(item)
for city in cities:
  print([city])
