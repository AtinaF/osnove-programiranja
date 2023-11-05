# #beginner python exercises from practicepython.org
#
# #01 Character input
# #Create a program that asks the user to enter their name and their age.
# # Print out a message addressed to them that tells them the year that
# # they will turn 100 years old.
# #Extras:
# # 1. Add on to the previous program by asking the user for another number
# # and printing out that many copies of the previous message.
# # (Hint: order of operations exists in Python)
# # 2. Print out that many copies of the previous message on separate lines.
# # (Hint: the string "\n is the same as pressing the ENTER button)
#
# name = input("Enter your name: ")
# age = eval(input("Enter your age: "))
# message = name + ", you will turn 100 in the year " + str(100-age)
# print(message)
# repetition = eval(input("How many times would you like to print that message?"))
# for i in range(repetition):
#     print(message)
#
# # another way of doing this:
#     print(repetition * message) #output format: message, message, message
#
# #02 Ask the user for a number. Depending on whether the number is even or odd,
# # print out an appropriate message to the user.
# #Extras:
#     # 1. If the number is a multiple of 4, print out a different message.
#     #2. Ask the user for two numbers: one number to check (call it num)
#     #and one number to divide by (check). If check divides evenly into num,
#     # tell that to the user. If not, print a different appropriate message.
#
# user_input = eval(input("Enter a number: "))
# if(user_input %2 == 0):
#     print("The number you have entered, is even.")
# else:
#     print("The number you have entered, is odd.")
#
# if(user_input %4 == 0):
#     print("The number you have entered, is a multiple of 4.")
#
# num, check = eval(input("Enter a number to check, and a number to divide by: "))
# remainder = num % check;
# if(remainder == 0):
#     print("numbers divide evenly")
# else:
#     print("numbers don't divide.")
import math
import random

# #03 Take a list, say for example this one: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# # and write a program that prints out all the elements of the list that are less than 5.
# # Extras:
# # 1. Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# # 2. Write this in one line of Python.
# # 3. Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = []
# # for i in a:
# #     print(i)    #prints elements of array
# for i in range(len(a)):
#     if(a[i]<5):
#         # print(a[i])
#         b.append(a[i])
# print(b)
#
# c = [element for element in a if element < 5]
# print(c)
#
# user_input = eval(input("Enter a number: "))
# result = [element for element in a if element < user_input]
# print(result)

# #04 Create a program that asks the user for a number and then prints out a list of all
# #  the divisors of that number.
#
# user_input = eval(input("Enter a number: "))
# result = []
# for i in range(user_input):
#     if user_input % (i+1) == 0:
#         result.append(i+1)
# print(result)

# #05 Take two lists, say for example these two:
# # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# # b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# # and write a program that returns a list that contains only the elements
# # that are common between the lists (without duplicates).
# # Make sure your program works on two lists of different sizes.
# # Extras:
# # 1. Randomly generate two lists to test this
# # 2. Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
#
# # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# # b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# a, b = [], []
# for i in range(15):
#     a.append(math.floor(random.random()*10))
#     b.append(math.floor(random.random()*10))
#
# print(a, "\n", b)
#
# # for every element in longer list, check if that element exists in shorter list, and add it to resulting array, if it does.
# result = [element for element in (b,a)[len(b)>len(a)] if (a,b)[len(b)>len(a)].__contains__(element)]
# print(result)

# #06 Ask the user for a string and print out whether this string is a palindrome or not.
# # (A palindrome is a string that reads the same forwards and backwards.)
#
# user_input_string = input("Enter the string you wish to perform palindrome check on: ")
# is_palindrome = True
#
# for i in range(math.ceil(len(user_input_string)/2)):
#     if user_input_string[i] != user_input_string[len(user_input_string)-1-i]:
#         print(user_input_string[i], "...", user_input_string[len(user_input_string)-1-i])
#         is_palindrome = False
#
# if is_palindrome:
#     print("palindrome.")
# else:
#     print("not palindrome.")

# #07 Let’s say I give you a list saved in a variable:
# # a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# # Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
#
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# b = [element for element in a if element%2==0]
# print(b)

# # 08 Make a two-player Rock-Paper-Scissors game.
# # (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
# # Rock beats scissors
# # Scissors beats paper
# # Paper beats rock
#
# a = "y"
# while a != "n":
#     winner = -1
#     first_user_input = input("<User1> Enter R for ROCK, P for PAPER, S for SCISSORS: ")
#     second_user_input = input("<User2> Enter R for ROCK, P for PAPER, S for SCISSORS: ")
#
#     if first_user_input == second_user_input:
#         winner = 0
#     elif first_user_input == "R" and second_user_input == "P":
#         winner = 2
#     elif first_user_input == "R" and second_user_input == "S":
#         winner = 1
#     elif first_user_input == "P" and second_user_input == "R":
#         winner = 1
#     elif first_user_input == "P" and second_user_input == "S":
#         winner = 2
#     elif first_user_input == "S" and second_user_input == "R":
#         winner = 2
#     elif first_user_input == "S" and second_user_input == "P":
#         winner = 1
#
#     if winner == 0:
#         print("It's a draw")
#     else:
#         print("The winner is: <User", winner, "> ")
#     a = input("Do you want to keep playing? y:n ")

# # 09 Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
# # then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)
# # Extras:
# # 1. Keep the game going until the user types “exit”
# # 2. Keep track of how many guesses the user has taken, and when the game ends, print this out.
#
# user_input = ""
# number_of_tries = 0
# number_was_guessed = False
# num = random.randint(1, 9)
#
# while user_input != "exit":
#     if number_was_guessed:
#         num = random.randint(1, 9)
#         number_of_tries = 0
#     guess = eval(input("Guess a number between 1 and 9 "))
#     number_of_tries += 1
#     if guess == num:
#         print("You guessed it!")
#         number_was_guessed = True
#     elif guess > num:
#         print("You guessed too high.")
#     else:
#         print("You guessed too low.")
#     user_input = input("Type anything to play, or exit to quit ")
#
# print("Number of tries: ", number_of_tries)

# #10 This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.
# # Take two lists, say for example these two:
# #
# # 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# # 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# #
# # and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# # Make sure your program works on two lists of different sizes.
# # Write this using at least one list comprehension.
# # Extra:
# # Randomly generate two lists to test this
#
# # creating 2 lists, random lengths, fill them with random elements
# a, b = [], []
# list1_length = math.floor(random.randint(5, 20))
# list2_length = math.floor(random.randint(5, 20))
#
# for i in range(list1_length):
#     a.append(math.floor(random.randint(1, 50)))
# for i in range(list2_length):
#     b.append(math.floor(random.randint(1, 50)))
#
# print( a, "\n", b)
#
# # for every element in longer list(if lists are not equal length), check if that element exists in shorter list, and add it to resulting array, if it does.
# result = [element for element in b if a.__contains__(element)]
# print(result)
#
# result_with_no_duplicates = [];
# for i in range(len(result)):
#     if not result_with_no_duplicates.__contains__(result[i]):
#         result_with_no_duplicates.append(result[i])
#
# print(result_with_no_duplicates)

# 11 Ask the user for a number and determine whether the number is prime or not.
# You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.
#
# def is_prime(number):
#     result = []
#     for i in range(number):
#         if number % (i + 1) == 0:
#             result.append(i+1)
#     print(result)
#     if len(result)==2:
#         return True
#     else:
#         return False
#
# user_input = eval(input("Enter a number: "))
# if is_prime(user_input):
#     print("This number is prime.")
# else:
#     print("This number is not a prime.")

# #12 Write a program that takes a list of numbers
# # (for example, a = [5, 10, 15, 20, 25]) and makes a
# # new list of only the first and last elements of the given list.
# # For practice, write this code inside a function.
#
# def get_first_and_last_element(list):
#     if list != None:
#         return [list[0], list[len(list)-1]]
#         # return [list[0], list[-1]]   #drugi nacin
#     else:
#         return -1
#
# a = [5, 10, 15, 20, 25]
# b = get_first_and_last_element(a)
# print(b)

# #13 Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# # Take this opportunity to think about how you can use functions.
# # Make sure to ask the user to enter the number of numbers in the sequence to generate.
# # (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence
# # is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
#
# number_of_fibonnaci_elements = eval(input("Enter how many Fibonnaci numbers you'd like to get: "))
# def get_fibonnaci_numbers(how_many):
#     if how_many <= 1:
#         return [1]
#     elif how_many == 2:
#         return [1, 1]
#     else:
#         result = [1, 1]
#         for i in range(1, how_many-1):
#             result.append(result[i-1]+result[i])
#     return result
#
# print(get_fibonnaci_numbers(number_of_fibonnaci_elements))

# # 14 Write a program (function!) that takes a list and returns a new list that contains
# # all the elements of the first list minus all the duplicates.
# # Extras:
# # Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# # Go back and do Exercise 5 using sets, and write the solution for that in a different function.
#
# list1 = []
# for i in range(15):
#     list1.append(random.randint(1, 30))
#
#
# def remove_duplicates(some_list):
#     result = []
#     for i in range(len(some_list)):
#         if not result.__contains__(some_list[i]):
#             result.append(some_list[i])
#     return result
#
# print(list1)
# list2 = remove_duplicates(list1)
# print(list2)
#
# # set is a collection where no element repeats, and there is no "indexing", set[3] means nothibg
# def remove_duplicates_using_sets(some_list):
#     return set(some_list)
#
# print(remove_duplicates_using_sets(list1))
#
# #exercise 5 with sets:
# a, b = [], []
# for i in range(15):
#     a.append(math.floor(random.random()*10))
#     b.append(math.floor(random.random()*10))
# print(a, "\n", b)
# result = list(set(a + b))
# print(result)

# 15