#!/usr/bin/env python
def does_it_contain(str, array):
    if int(array.find(str)) != -1:
        return True
    else:
        return False

print("Let's create a list of 5 things. Think of a general category.")
category = input("What category of things should we store? ")
list = []
check_if_contains = []
for i in range(5):
    element = input(str(category) + " " + str(int(i + 1)) + ": ")
    list.append(element)


chosen_element = int(input("\nPick a number between 1 and 5: "))
print("You picked " + str(list[int(chosen_element - 1)]) + "!")


print("\nThe sorted list is:")
print(list)

char = input("\nPick a character: ")
for j in range(5):
    answer = does_it_contain(char,list[j])
    check_if_contains.append(answer)
print(check_if_contains)