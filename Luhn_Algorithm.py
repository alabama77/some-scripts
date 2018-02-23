def validate(numbers):
	numbers = str(numbers)
	numbers = [int(i) for i in numbers]
	numbers.reverse()

	for element in range(1, len(numbers), 2):
		numbers[element] *= 2
		
			if numbers[element] > 9:
				numbers[element] = int(str(numbers[element])[0]) + int(str(numbers[element])[1])

	result = 0
	
	for number in range(0, len(numbers)):
		result += numbers[number]
	
	if result % 10 == 0:
		return True
	else:
		return False
