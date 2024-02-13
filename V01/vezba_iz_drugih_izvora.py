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

# # 15 Write a program (using functions!) that asks the user for a long string containing multiple words.
# # Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
# #   My name is Michele
# # Then I would see the string:
# #   Michele is name My
# # shown back to me.
#
# user_input = input("Enter a string: ")
# # substrings = user_input.split(" ")
# substrings = [s.strip() for s in user_input.split(',')]
# backwards_string = substrings[::-1]
# print(backwards_string)

# #16 Note: this is a 4-chili exercise, not because it introduces a concept, but because this exercise is more like a project.
# # Feel free to skip this and come back when you’re more ready!
# # Write a password generator in Python. Be creative with how you generate passwords
# # - strong passwords have a mix of lowercase letters, uppercase letters, numbers,
# # and symbols. The passwords should be random, generating a new password every time
# # the user asks for a new password. Include your run-time code in a main method.
# # Extra:
# #  Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
#
#
# def generate_values(is_password_weak):
#     # list(map(chr, range(ord('a'), ord('z')+1)))
#     lower_case = list(map(chr, range(97, 123)))
#     upper_case = list(map(chr, range(65, 91)))
#     digits = ['0' ,'1', '2', '3', '4', '5', '6', '7', '8', '9']
#     special_characters = list(map(chr, range(33, 48)))
#
#     if not is_password_weak:
#         values = lower_case + upper_case + digits + special_characters
#     else:
#         values = lower_case + upper_case
#
#     return values
#
#
# def generate_password(is_weak):
#     password = ""
#     values = generate_values(is_weak)
#     for i in range(30):
#         # password += values[random.randint(0, values.__len__()-1)]
#         password+=random.choice(values)
#     return password
#
#
# command = ""
# while command != 'N':
#     command = input("Generate password? y:n >> ").upper()
#     if command != 'N' and command != 'Y':
#         print("Wrong command.")
#     elif command == 'Y':
#         option = input("How strong do you want your password to be? \n1. strong\n2. weak \n>> ")
#         if option != "1" and option != "2":
#             print("Wrong option.")
#         else:
#             print("Your password is: ", generate_password(option=="2"))


# #17 Note: this is a 4-chili exercise, not because it introduces a concept (although it introduces a new library),
# # but because this exercise is more like a project. Feel free to skip this and come back when you’re more ready!
# # Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
# # Concepts for this week:
# #
# #     Libraries
# #     requests
# #     BeautifulSoup
#
# import requests
# from bs4 import BeautifulSoup
#
# url = "https://www.nytimes.com/"
# response = requests.get(url)
# website_html = response.text
#
# soup = BeautifulSoup(website_html, features="lxml")
# title = soup.find('title').string
# print(title)


# #from bs4 import BeautifulSoup
# soup = BeautifulSoup(html_doc, 'html.parser')
#
# print(soup.prettify())
#
# <html>
#  <head>
#   <title>
#    The Dormouse's story
#   </title>
#  </head>
#  <body>
#   <p class="title">
#    <b>
#     The Dormouse's story
#    </b>
#   </p>
#   <p class="story">
#    Once upon a time there were three little sisters; and their names were
#    <a class="sister" href="http://example.com/elsie" id="link1">
#     Elsie
#    </a>
#    ,
#    <a class="sister" href="http://example.com/lacie" id="link2">
#     Lacie
#    </a>
#    and
#    <a class="sister" href="http://example.com/tillie" id="link2">
#     Tillie
#    </a>
#    ; and they lived at the bottom of a well.
#   </p>
#   <p class="story">
#    ...
#   </p>
#  </body>
# </html>

# soup.title
# # <title>The Dormouse's story</title>
#
# soup.title.name
# # u'title'
#
# soup.title.string
# # u'The Dormouse's story'
#
# soup.title.parent.name
# # u'head'
#
# soup.p
# # <p class="title"><b>The Dormouse's story</b></p>
#
# soup.p['class']
# # u'title'
#
# soup.a
# # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
#
# soup.find_all('a')
# # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
#
# soup.find(id="link3")
# # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>


# #18 Create a program that will play the “cows and bulls” game with the user. The game works like this:
# # Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
# # For every digit that the user guessed correctly in the correct place, they have a “cow”.
# # For every digit the user guessed correctly in the wrong place is a “bull.”
# # Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
# # Once the user guesses the correct number, the game is over.
# # Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
# #
# # Say the number generated by the computer is 1038. An example interaction could look like this:
# #   Welcome to the Cows and Bulls Game!
# #   Enter a number:
# #   >>> 1234
# #   2 cows, 0 bulls
# #   >>> 1256
# #   1 cow, 1 bull
# #   ...
# #
# # Until the user guesses the number.
#
# generated_number = (random.randint(1000, 9999)).__str__()
# print(generated_number)
# guess = ""
# number_of_guesses = 0
# while guess != generated_number:
#     guess = input("Enter a 4-digit number: >> ").strip()
#     number_of_guesses += 1
#     bulls = 0
#     cows = 0
#     for i in range(generated_number.__len__()):
#         if generated_number.__contains__(guess[i]) and generated_number[i] == guess[i]:
#             cows += 1
#         elif generated_number.__contains__(guess[i]) and generated_number[i] != guess[i]:
#             bulls += 1
#     print("{} cows, {} bulls ".format(cows, bulls))
#
# print("You guessed the number in {0} tries. ".format(number_of_guesses))


# #19 Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article
# # on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
# # The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen
# # so that you can read the full article without having to click any buttons.
# # (Hint: The post here describes in detail how to use the BeautifulSoup and requests libraries through
# # the solution of the exercise posted here.)
# #
# # This will just print the full text of the article to the screen.
# # It will not make it easy to read, so next exercise we will learn how to write this text to a .txt file.
#
# import requests
# from bs4 import BeautifulSoup
#
# url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
# response = requests.get(url)
# page_html = response.text
#
# soup = BeautifulSoup(page_html, features="lxml")
# elements = soup.find_all(class_ ='BodyWrapper-kufPGa fxGCxI body body__container article__body');
#
# text = ""
#
# for div in elements:
#     for inner_div in div.contents:
#         # print(inner_div)
#         all_children_p_tags = inner_div.find_all('p')
#         for p in all_children_p_tags:
#             text += p.text + "\n"
#
# print(text)


# #20 Write a function that takes an ordered list of numbers
# # (a list where the elements are in order from smallest to largest) and another number.
# # The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
# # Extras:
# # use binary search.
#
# def contains_number(ordered_list, number):
#     if number < ordered_list[0] or number > ordered_list[len(ordered_list)-1]:
#         return False
#     else:
#         return search(0, len(ordered_list), ordered_list, number)
#
#
# def search(start, end, ordered_list, number):
#     median_index = math.floor((start+end)/2)
#     median = ordered_list[median_index]
#
#     if number == median:
#         return True
#     elif end == start + 1:
#         return False
#     elif number > median:
#         return search(median_index, end, ordered_list, number)
#     elif number < median:
#         return search(start, median_index, ordered_list, number)
#
#
# list1 = list(random.randint(10, 70) for i in range(50))
# list1.sort()
# print(list1)
# print(contains_number(list1, 57))

# # 21 Take the code from the How To Decode A Website exercise
# # (if you didn’t do it or just want to play with some different code,
# # use the code from the solution), and instead of printing the results
# # to a screen, write the results to a txt file. In your code, just
# # make up a name for the file you are saving to.
# # Extras:
# #     Ask the user to specify the name of the output file that will be saved.
#
# import requests
# from bs4 import BeautifulSoup
# from os.path import exists
#
#
# url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
# result = requests.get(url)
# page_html = result.text
#
# soup = BeautifulSoup(page_html, features='lxml')
# elements = soup.find_all(class_ ='BodyWrapper-kufPGa fxGCxI body body__container article__body')
# text = ""
#
# for div in elements:
#     for inner_div in div.contents:
#         paragraphs = inner_div.find_all('p')
#         for p in paragraphs:
#             text += p.text + "\n"
#
# file_name = input("Enter file name >> ")
# if not exists(file_name):
#     open(file_name, 'w').close()
#
# file = open(file_name, 'w')
# file.write(text)
# file.close()


#22 Given a .txt file that has a list of a bunch of names, count how many of each name there
# are in the file, and print out the results to the screen. I have a .txt file for you, if you want to use it!
# Extra:
#     Instead of using the .txt file from above (or instead of, if you want the challenge),
#     take this .txt file, and count how many of each “category” of each image there are.
#     This text file is actually a list of files corresponding to the SUN database scene
#     recognition database, and lists the file directory hierarchy for the images. Once
#     you take a look at the first line or two of the file, it will be clear which part
#     represents the scene category. To do this, you’re going to have to remember a bit
#     about string parsing in Python 3. I talked a little bit about it in this post.

# from os.path import exists
#
# file_name = "22_names.txt"
# names = []
#
# if not exists(file_name):
#     open(file_name, 'w').close()
#
# file = open(file_name, 'r')
# for line in file.readlines():
#     names.append(line[:-1])
# file.close()
#
# unique_names = set(names)
# dict = {}
#
# for name in names:
#     if name in dict:
#         dict[name] += 1
#     else:
#         dict[name] = 1
#
# print(dict)

# from os.path import exists
#
# file_name = "22_categories.txt"
# if not exists(file_name):
#     open(file_name, 'w').close()
#
# file_paths = []
# file = open(file_name, 'r')
# for line in file.readlines():
#     if line != "":
#         file_paths.append(line)
# file.close()
#
# categories = {}
#
# for file_path in file_paths:
#     category = file_path.split('/')[2]
#     if category in categories:
#         categories[category] += 1
#     else:
#         categories[category] = 1
#
# print(categories)

# # 23 Given two .txt files that have lists of numbers in them, find the numbers that
# # are overlapping. One .txt file has a list of all prime numbers under 1000, and the
# # other .txt file has a list of happy numbers up to 1000.
#
# from os.path import  exists
#
# primes_file = "primes.txt"
# happy_numbers_file = "happy_numbers.txt"
#
#
# def get_numbers_from_file(filename):
#     result = []
#     if exists(filename):
#         file = open(filename, 'r')
#         for line in file.readlines():
#             if line != '\n':
#                 result.append(line[:-1])
#         file.close()
#     return result
#
#
# def get_duplicates(list_a, list_b):
#     duplicates = []
#     for element in list_a:
#         if list_b.__contains__(element):
#             duplicates.append(element)
#     return duplicates
#
#
# primes = get_numbers_from_file(primes_file)
# happy_numbers = get_numbers_from_file(happy_numbers_file)
# print(primes)
# print("Duplicates found: \n {}".format(set(get_duplicates(primes, happy_numbers))))

# # 24 In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.
# # This time, we’re going to do exactly the opposite. You, the user, will have in your head a number
# # between 0 and 100. The program will guess a number, and you, the user, will say whether it is too high,
# # too low, or your number.
# # At the end of this exchange, your program should print out how many guesses it took to get your number.
#
#
# possibilities = list(range(100))
#
# user_input = ""
# guess = possibilities[math.floor(len(possibilities)/2)]
# number_of_guesses = 0
# start = 0
# end = len(possibilities)-1
#
#
# def get_next_element(start, end, values):
#     middle_index = math.floor((start+end)/2)
#     return values[middle_index]
#
#
# while user_input.lower() != 'yes':
#     number_of_guesses += 1
#     user_input = input("Is this your number? {}\n[yes/no]>>".format(guess))
#     if user_input != 'yes':
#         user_input = input("Is your number lower [<] or greater [>] than {}?\nType '<' or '>'\n>> ".format(guess))
#         if user_input == '>':
#             start = possibilities.index(guess)
#             guess = get_next_element(start, end, possibilities)
#         elif user_input == '<':
#             end = possibilities.index(guess)
#             guess = get_next_element(start, end, possibilities)
#         else:
#             print("Wrong input. ")
#
# print("Number guessed: {}\n Number of guesses: {}".format(guess, number_of_guesses))

# #25 As you may have guessed, we are trying to build up to a full tic-tac-toe board.
# # However, this is significantly more than half an hour of coding, so we’re doing it in pieces.
# #
# # Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe,
# # not worrying about how the moves were made.
# # If a game of Tic Tac Toe is represented as a list of lists, like so:
# # game = [[1, 2, 0],
# # 	[2, 1, 0],
# # 	[2, 1, 1]]
# #
# # where a 0 means an empty square, a 1 means that player 1 put their token in that space,
# # and a 2 means that player 2 put their token in that space.
# #
# # Your task: given a 3 by 3 list of lists that represents a Tic Tac Toe game board,
# # tell me whether anyone has won, and tell me which player won, if any.
# # A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal.
# # Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.
#
# game = [[2, 1, 0],
#         [1, 2, 0],
#         [2, 2, 2]]
#
# def find_winner(game):
#     winner = 0
#
#     for i in range(3):
#         # row has winner:
#         if game[i][0] == game[i][1] == game[i][2] != 0:
#             winner = game[i][0]
#             #column
#         elif game[0][i] == game[1][i] == game[2][i] != 0:
#             winner = game[0][i]
#
#     #diagonal
#     if game[0][0] == game[1][1] == game[2][2] != 0:
#         winner = game[0][0]
#
#     return winner
#
#
# winner = find_winner(game)
# if winner == 0:
#     print("There are no winners.")
# else:
#     print("The winner is: {}".format(winner))


