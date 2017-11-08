#!/usr/bin/env python
import sys
from collections import Counter

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
# This function takes an inputed year and then returns all makes and models from that year

def toyotas_past_2000():
    total = 0
    for i in range(0, len(id_number)):
        if year[i] > "2000" and make[i] == "Toyota":
            total = total + 1
    print "%d Toyotas in the list past 2000" % total
#This function counts all Toyotas in the list owned past the year 2000

def popular_color():
    color_counts = Counter(color)
    list(color_counts)
    most_c_color = max(color_counts)
    color_total = color.count(most_c_color)
    print ("The most common color is %s with a total count of %d") % (most_c_color, color_total)

def car_colors():
    color_counts = Counter(color)
    c_list = list(color_counts)
    return c_list

def car_colors_counts():
    
