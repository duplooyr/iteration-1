# iteration pattern
#doing the same thing once for each member of a list

# [1, 5, 7 ,8 , 4, 3]

def print_list(list):
	# standard for loop with range
	# for i in range(0, len(list)):
	# 	print list[i]

	# for each loop
	for item in list:
		print item
def add_one(list):
	#standard for loop with range
	for i in range(0, len(list)):
		list[i] += 1
	return list

def print_scores(names, scores):
	for i in range(0, len(names)):
		print names[i] , " scored " , scores[i]


# filter pattern
# exlude a calculation from list members.
def congratulations(names, scores):
	for i in range(0, len(names)):
		if (scores[i] == 100):
			print "Congrats", names[i], "! You got a perfect score!"



# accumulation pattern - a type of iteration
# keep track of other data as we go
# def sum(list):
# 	total = 0
# 	for n in numbers:
# 		total += n
# 	return total

# def max(numbers):
# 	current_max = numbers[0]
# 	for n in numbers:
# 		if n > current_max:
# 			current_max = n
# 	return current_max

def avg(list):
	return float(sum(list)) / len(list)

def drop_2_average(list):
	list.sort()
	return float(sum(list[2:])) / len(list[2:])

def alternating_sum(list):
	total = 0
	for i in range(0, len(list)):
		if i % 2 == 0:
			total += list[i]
		else: 
			total -= list[i]

	return total

def sum_outside(list,min,max):
	list.sort()
	total = sum(list[ :min]) + max + sum(list[max: ]) - min
	return total