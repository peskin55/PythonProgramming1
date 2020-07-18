#!/usr/bin/env python
roster_file = input("Hello.\nPlease enter a roster file: ")
count = len(open(roster_file).readlines()) - 1
load = open(roster_file,'r')
header = load.readline()[:-1]
data = []
for i in range(count):
	data_import = load.readline()[:-1]
	data.append(data_import.split(","))
append_file = input("There are " + str(count) + " names in this file. Would you like to enter additional names? (Y/N)")
if append_file in ["Y",'y']:
	amount = int(input("How many more names? "))
	for name in range(amount):
		print("----- Person " + str(name + 1) " -----")
		fn = input("First Name: ")
		ln = input("Last Name: ")
		job = input("Occupation: ")
		ht = int(input("Height (in inches): "))
		wt = int(input("Weight (in pounds): "))
		data.append([fn,ln,job,ht,wt])
else:
	amount = 0
new_file = input("-------------------------\nSave new roster file as: ")
export = open(new_file,'w')
row_format = '{:12} {:12} {:3} {:15} {:5} {:3}'
export.writelines(row_format.format(header[0],header[1],header[2],header[3],header[4],header[5]))
for line in range(count + amount):
	export.writelines(row_format.format(data[line][0],data[line][1],data[line][2],data[line][3],data[line][4],data[line][5]))
