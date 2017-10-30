def is_great(number):
	digits = []

	while number>0:
		digit = number % 10
		digits.append(digit)
		number //= 10
	
	nd = len(digits)
	incl = [0]*nd

	for i in range(nd):
		indexes = []
		dsum = 0
		j = i
		while dsum<10 and j<nd:
			dsum += digits[j]
			indexes.append(j)
			j += 1
		if dsum==10:
			for k in range(len(indexes)):
				incl[indexes[k]] += 1

	return all(incl)

n_great = 0
for x in range(1,6000000+1):
	if is_great(x):
		n_great += 1

print(n_great)
