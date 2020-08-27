#!/usr/bin/env python
file_name = input("Please enter a file name: ")
# Number of lines, excluding the header is counted below
line_count = len(open(file_name).readlines()) - 1

data_load = open(file_name,"r")
# Text file is open for reading and is ready to have its data imported
data = []
imported_terms = []
converted_data = []
# Don't need to import the header line
skip_header = data_load.readline()
for i in range(line_count):
# Importing each line of the text file as a list
# Stripping any regex from the data
    line = data_load.readline()[:-1]
    data.append(line.split("\t",1))
    imported_terms.append(line.split("\t",1)[0])
add_more = input("There are 10 terms in this vocabulary list.\nWould you like to add more terms (Y/N)? ")
while add_more in ["Yes","Y","yes","y"]:
    amount = input("How many would you like to add? ")
    try:
# Only allowing positive integers as a valid input, question repeats until
# a valid input is received
        int_amount = int(amount)
        if int_amount <= 0:
            print("Error. Please enter a positive number.")
            continue
        else:
            for i in range(int_amount):
# User will have the ability to edit data from imported file
                term = input("Term #" + str(i + 1) + ": ")
                if term in imported_terms:
                    update = input("Warning! This term is already in the vocabulary list. Update definition (Y/N)? ")
                    if update in ["Yes","Y","yes","y"]:
                        term_index = imported_terms.index(term)
                        data.pop(term_index)
                        dest = input("Destination #" + str(i + 1) + ": ")
                        data.insert(term_index, [term, dest])
                        continue
                    else:
                        continue
                else:
                    dest = input("Destination #" + str(i + 1) + ": ")
                    data.append([term, dest])
                    imported_terms.append(term)
                    continue
    except ValueError:
# If a non integer is inputted, the progran will not exit
# It will print an error message and request a valid input
        print("Error. Please enter an integer.")
        continue
# User will have the option to end loop below
    add_more = input("Would you like to add more terms (Y/N)? ")
print("There are " + str(len(data)) + " terms in the new vocabulary list.\n")
for j in range(len(data)):
# Data is joined and printed in a reader friendly format
    converted_data.append(data[j][0] + " - " + data[j][1] + "\n")
    print(converted_data[j][:-1])
save_file = input("\nWhat would you like to save the file as? ")
data_export = open(save_file,"w")
data_export.writelines("term - definition\n")
for k in range(len(converted_data)):
# Consolidated data is written to file of user's choice
    data_export.writelines(converted_data[k])
