from itertools import count


def next_turn(M, i, j, n, counter):
	# go down
	for i in range(i, i+n-1):
		M[i][j] = next(counter)
	# go left
	j -= 1
	for j in range(j, j-(n-1), -1):
		M[i][j] = next(counter)
	# go up
	i -= 1
	for i in range(i, i-(n-1), -1):
		M[i][j] = next(counter)
	# go right
	j += 1
	for j in range(j,j+n-1):
		M[i][j] = next(counter)
	return i, j


def main():
	N = 1169
	ci, cj = N//2, N//2
	M = [[0]*N for i in range(N)]
	counter = count(1)
	M[ci][cj] = next(counter)
	n = 3
	while n<=N:
		cj += 1
		ci, cj = next_turn(M, ci, cj, n, counter)
		n += 2
	result = sum(M[i][i] for i in range(N))+sum(M[i][N-i-1] for i in range(N))-1
	print(result)


if __name__ == '__main__':
	main()
