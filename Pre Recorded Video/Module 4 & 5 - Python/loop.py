fruits = [
    "Apple",
    "Banana",
    "Orange",
    "Watermelon",
    "Pineapple",
    "Mango"
]
print("-----------------------------------------------------------------------------------")
for fruit in fruits:
    print(fruit)
print("-----------------------------------------------------------------------------------")
for i in range(5):
    print(i)
print("-----------------------------------------------------------------------------------")
for i in range(len(fruits)):
    print(fruits[i])
print("-----------------------------------------------------------------------------------")
for i in range(1, 6):
    print(i)
print("-----------------------------------------------------------------------------------")
for i in range(2, 11, 2):
    print(i)
print("-----------------------------------------------------------------------------------")
n = int(input("input a Number: "))
for i in range(1, 11):
    print(f"{n} X {i} = {n*i}")
print("-----------------------------------------------------------------------------------")
n = int(input("input a Number: (0 to exit): "))
while n!=0:
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")
    n = int(input("input a Number: (0 to exit): ")) 
print("-----------------------------------------------------------------------------------")
while True:
    s = input()
    print(s.upper())
    s = input("Do you want to continue (y/n)?")
    if s == 'y':
        continue # Skipes codes after continue
    print("Bye Bye :)")
    break