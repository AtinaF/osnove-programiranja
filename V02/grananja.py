# A

counter = 1
maximum = 5
while counter != 0:
    print(counter * "*")
    if counter < maximum:
        counter += 1
    if counter == maximum:
        break

while counter != 0:
    print(counter * "*")
    counter -= 1

# B
# cntr = 7
# counter = 0
# while cntr>0:
#     if counter % 6 == 0:
#         print(6*"*")
#     elif counter % 3 == 0:
#         print(3*"*")
#     else:
#         print("*")
#     cntr -= 1
#     counter += 1

# C
print("  ***")
counter = 0
while counter < 6:
    if counter == 2:
        print(5*"*")
    else:
        print("*   *")
    counter += 1