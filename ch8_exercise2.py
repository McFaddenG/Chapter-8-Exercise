fhand = open('ch8_exercise.txt')
count = 0
for line in fhand:
	words = line.split()
	# print('Debug: ', words)
	if len(words) < 3 : continue
	if words[0] != 'From' : continue
	print(words[2])

#Changed len(words) == 0 : to len(words) < 3 : to prevent IndexError