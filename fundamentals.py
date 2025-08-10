import random
# name = input("What is your name? ")
# age = input("What is your age? ")
# color = input("What is your facourite color? ")
# print(name)
# print(age)
# print(color)



# score = int(input("Score: "))
# if score>90:
#     print("Excellent")
# elif score>70:
#     print("Good")
# else:
#     print("Needs Improvement")



# first_name = "Dhanushka"
# last_name = "Chandimal"
# full_name = first_name + " " + last_name
# multi_line = """This is first line 
# This is second line"""
# print(full_name)
# print("length of name = " + str(len(full_name)))
# print(full_name[0])
# print(multi_line)
# print("wow! " * 3)
# print(full_name[1:4])
# print(full_name[3:])
# print(full_name[:5])
# print(full_name[-1])
# print(full_name[-3])
# print(full_name.upper())
# print(full_name.lower())

# string = "            test           "
# print(">>>" + string + "<<<")
# print(">>>" + string.strip() + "<<<")

# string = "This is original text.pdf"
# print(string)
# print(string.replace("original", "replaced"))
# print(string.split())
# print(string.split("a"))

# list1 = ["1", "23", "asdsa"]
# print(" ".join(list1))

# print(string.endswith(".pdf"))
# print(string.endswith(".gif"))
# print(string.endswith("f"))

# age = 30

# print("My name is {} and I am {} years old.".format(first_name, age))
# print("My name is {}.".format(first_name, age))
# # print("My name is {} and I am {} years old.".format(first_name))
# print(f"My name is {first_name} and I am {age} years old.")

# first_names = ["Christian", "Dylan", "Travis", "Katelyn"]
# last_names = ["Sachs", "Katina", "Peck", "Mehner"]

# print("Random name: " + first_names[random.randint(0,len(first_names)-1)] + " " + last_names[random.randint(0,len(last_names)-1)])
# print("Random name: " + random.choice(first_names) + " " + random.choice(last_names))



# x = 20
# y = 3
# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x // y)
# print(x % y)
# print(x ** y)
# print(pow(x,y))
# print(abs(-15))
# print(round(-15.2))
# print(round(-15.6))
# print(round(15.2))
# print(round(15.6))
# print(int("256") + 1)

# print(7 % 3)
# print(-7 % 3)
# print(7 % -3)
# print(-7 % -3)

# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# print(f"{num1} + {num2} = {num1 + num2}")
# print(f"{num1} - {num2} = {num1 - num2}")
# print(f"{num1} * {num2} = {num1 * num2}")
# print(f"{num1} / {num2} = {num1 / num2}")



# user_weather = input("Is it sunny or raining? ")
# user_mood = input("Are you happy or tired? ")

# if(user_weather == "sunny" and user_mood == "happy"):
#     print("Go for a hike!")
# else:
#     print("Relax indoors.")

# random_number = random.randint(1,10)
# user_input = int(input())
# if(random_number > user_input):
#     print("too low")
#     user_input = int(input())
# elif(random_number < user_input):
#     print("too high")
#     user_input = int(input())
# else:
#     print("Congratulations you guessed corectly")



# my_list = [1, 2.34, "Srtring", True, 3, 4, 5, 6]

# print(my_list[0])
# print(my_list[1])
# print(my_list[-1])
# print(my_list[-2])
# print(my_list[-3])

# my_list.append("del")
# print(my_list)

# my_list.insert(2,"del")
# print(my_list)

# my_list.remove("del") # remove only first matching item
# print(my_list)

# del my_list[0]
# print(my_list)

# print(my_list.pop(1))
# print(my_list)

# print(my_list[1:5])
# print(my_list[:3])
# print(my_list[3:])
# print(my_list[3:3])

# fruits = ["apple", "banana", "cherry", "date"]
# print(fruits[0])
# print(fruits[-1])
# fruits.append("elderberry")
# print(fruits)
# fruits.insert(1, "blueberry")
# print(fruits)
# fruits.remove("banana")
# print(fruits)
# del fruits[0]
# print(fruits)
# citrus_fruits = fruits[1:3]
# print(citrus_fruits)

# print(len(fruits))
# print(min(fruits))
# print(max(fruits))

# numbers = [55, 1, 5, 3, -50, -2]
# print(numbers)
# print(len(numbers))
# print(min(numbers))
# print(max(numbers))
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
# print(numbers + fruits)
# numbers.extend(fruits)
# print(numbers)

# nested_list = [[0, 1, 2], [11, 12, 13], [21, 22, 23]]
# print(nested_list)
# print(nested_list[1])
# print(nested_list[1][2])

# favourites_books = []
# favourites_books.append(input("Enter your first favourite book: "))
# favourites_books.append(input("Enter your second favourite book: "))
# favourites_books.append(input("Enter your third favourite book: "))
# print(favourites_books)
# favourites_books.sort()
# print(favourites_books)



# letters = ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"]
# for item in letters:
#     print(item)
# print("========================")
# for i in range(5):
#     print(i)
# print("========================")
# for i in range(2,5):
#     print(i)
# print("========================")
# for i in range(7,16,3):
#     print(i)
# print("========================")
    
# num = 2
# while(num<20):
#     print(num)
#     num+=2
# print("========================")

# for i in range(1, 31):
#     if(i%3==0):
#         continue
#     if(i>25):
#         break
#     print(i)



def introduce_yourself(name, hobby):
    print(f"Hello, {name}! As you mentioned your favourite hobby is {hobby}")

introduce_yourself("Dhanushka", "Coding")

def squareNum(*numbers):
    newList = []
    for i in numbers:
        newList.append(i**2)
    return newList

print(squareNum(3, 99, 12, 1, 7))