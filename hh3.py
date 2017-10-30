def is_palindrom(number):
	return str(number)==str(number)[::-1]


def reverse(number):
	return int(str(number)[::-1])


def operation(number):
	return number + reverse(number)


def fits(number):
	counter = 0
	inn = number
	while counter<=50:
		number = operation(number)
		if is_palindrom(number):
			break
		counter += 1
	if counter<=50:
		return False
	else:
		return True


def main():
	result = 0
	for x in range(1, 13110):
		if fits(x):
			result += 1
	print(result)


if __name__ == '__main__':
	main()
