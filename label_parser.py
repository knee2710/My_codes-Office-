import numpy as np
import itertools

a = [line.strip().split("#") for line in open('testing-labels-10263')]
 
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13] 

comb_1 = np.zeros(shape = (14,2))

one = 0
two = 0
three = 0

combinations_2 = [p for p in itertools.product(numbers, repeat = 2)]
combinations_3 = [p for p in itertools.product(numbers, repeat = 3)]

c_2 = np.asarray(combinations_2)
c_3 = np.asarray(combinations_3)

zeroes_2 = np.zeros((169,1))
zeroes_3 = np.zeros((2197,1))

comb_2 = np.append(combinations_2, zeroes_2, axis = 1)
comb_3 = np.append(combinations_3, zeroes_3, axis = 1)

training_one_card = open('training_one_card.txt', 'w')
training_two_card = open('training_two_card.txt', 'w')
training_three_card = open('training_three_card.txt', 'w')

for i in range(0, len(a)):
	if a[i][1] == '0 1 0 0 0 0 ':
		one = one + 1
		pos = a[i][2].find('1')/2
		comb_1[pos][0] = pos
		comb_1[pos][1] = comb_1[pos][1] + 1

	elif a[i][1] == '0 0 1 0 0 0 ':
		two = two + 1
		pos_1 = a[i][2].find('1')/2
		pos_2 = a[i][3].find('1')/2

		for i in xrange(len(c_2)):
			if c_2[i][0] == pos_1:
				if c_2[i][1] == pos_2:
					break

		comb_2[i][2] = comb_2[i][2] + 1

	elif a[i][1] == '0 0 0 1 0 0 ':
		three = three + 1
		pos_1 = a[i][2].find('1')/2
		pos_2 = a[i][3].find('1')/2
		pos_3 = a[i][4].find('1')/2

		for i in xrange(len(c_3)):
			if c_3[i][0] == pos_1:
				if c_3[i][1] == pos_2:
					if c_3[i][2] == pos_3:
						break

		comb_3[i][3] = comb_3[i][3] + 1
 
	

# To convert variables to integer data type
comb_1 = comb_1.astype(np.int64)
comb_2 = comb_2.astype(np.int64)
comb_3 = comb_3.astype(np.int64)

# Printing card combinations and number of cards
for i in  xrange(len(comb_1)):
	if comb_1[i][1] != 0:
		print "%d : %d" %(comb_1[i][0], comb_1[i][1])
		training_one_card.write(str(comb_1[i][0]) + " : " + str(comb_1[i][1]) + "\n")

for i in  xrange(len(comb_2)):
	if comb_2[i][2] != 0:
		print "%d + %d : %d" %(comb_2[i][0], comb_2[i][1], comb_2[i][2])
		training_two_card.write(str(comb_2[i][0]) + " + " + str(comb_2[i][1]) + " : " + str(comb_2[i][2]) + "\n")

for i in  xrange(len(comb_3)):
	if comb_3[i][3] != 0:
		print "%d + %d + %d : %d" %(comb_3[i][0], comb_3[i][1], comb_3[i][2], comb_3[i][3])
		training_three_card.write(str(comb_3[i][0]) + " + " + str(comb_3[i][1]) + " + " + str(comb_3[i][2]) + " : " + str(comb_3[i][3]) + "\n")

# To print number of cards
print str(one) " number of single card combinations"
print str(two) " number of double card combinations"
print str(three) " number of triple card combinations"