#!/usr/bin/env python
def equality_check(int1, int2):
    if int1 == int2:
        return True
    else:
        return False
numbers=[]
first = int(input("First Value: "))
second = int(input("Second Value: "))
numbers.append(first)
numbers.append(second)
addition = int(numbers[0] + numbers[1])
subtraction = int(numbers[0] - numbers[1])
comparison = equality_check(numbers[0],numbers[1])
print(str(numbers[0]) + " + " + str(numbers[1]) + " = " + str(addition))
print(str(numbers[0]) + " - " + str(numbers[1]) + " = " + str(subtraction))
print(str(numbers[0]) + " = " + str(numbers[1]) + " " + str(comparison))
if comparison == True:
    print(str(numbers[0]) + " is not equal to " + str(numbers[1]) + " False")
else:
    print(str(numbers[0]) + " is not equal to " + str(numbers[1]) + " True")
