#!/usr/bin/env python
import sys

data = open("MOCK_DATA.csv", 'r')
lines = data.readlines()

id_number = []
make = []
model = []
year = []
color = []
for i in range(1, len(lines)):
    info = lines[i].rstrip().split(",")
    id_number.append(info[0])
    make.append(info[1])
    model.append(info[2])
    year.append(info[3])
    color.append(info[4])


#////////2006 Make and Model//////////
# for i in range(0, len(id_number)):
#     if year[i] == "2006":
#         print make[i], model[i]

# Works for finding 2006 make and models only
#/////////////////////////////////////

def given_year():
    inputed_year = raw_input('Which year would you like make and models for? ')
    for i in range(0, len(id_number)):
        if year[i] == inputed_year:
            print inputed_year, make[i], model[i]
given_year() # This function takes an inputed year and then returns all makes and models from that year

def toyotas_past_2000():
    total = 0
    for i in range(0, len(id_number)):
        if year[i] > "2000" and make[i] == "Toyota":
            total = total + 1
    print "%d Toyotas in the list past 2000" % total
toyotas_past_2000() #This function counts all Toyotas in the list owned past the year 2000

