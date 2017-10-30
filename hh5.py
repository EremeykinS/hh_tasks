import math
import time
import concurrent.futures
from functools import lru_cache


@lru_cache(maxsize=65536)
def is_prime(x):
	"""возвращает True, если x является простым, иначе возвращает False"""
	if x==2:
		return True
	if x%2==0:
		return False
	prime = False
	for i in range(3, int(math.sqrt(x))+1, 2):
		if x%i==0:
			return False
	return True


@lru_cache(maxsize=65536)
def prime_factors(x):
	"""возвращает кортеж кортежей (f, k), где
	f - простой множитель числа x, k - его кратность"""
	if is_prime(x):
		return ((x, 1),)
	f = dict()
	i = 2
	pfmax = int(math.sqrt(x))+1
	while x>1 and i<=x:
		if x%i==0 and is_prime(i):
			if i in f:
				f[i] += 1
			else:
				f[i] = 1
			x = x//i
		else:
			i += 1 if i<5 else 2
	return tuple((k, f[k]) for k in f)


def s(n):
	"""возвращает наименьшее m, такое что m! делится без остатка на n"""
	if is_prime(n):
		return n
	pointers = []
	n_factors = prime_factors(n)
	for f,k in n_factors:
		m = f
		killed = 1
		while killed<k:
			m += f
			m_factors = dict(prime_factors(m))
			killed += m_factors[f]
		pointers.append(m)
	return max(pointers)


def S(t):
	"""S(M, N) = sum(s(n)) для всех n из [M, N]"""
	M, N = t
	su = 0
	for i in range(M,N+1):
		print(i-M)
		su += s(i)
	return su


def main():
	M = 6600000
	N = 6700000

	n_workers = 4
	start = time.time()
	results = []

	with concurrent.futures.ProcessPoolExecutor(max_workers=n_workers) as executor:
		d = int((N-M)/n_workers)
		ranges = [(M+i*d+1, M+(i+1)*d) for i in range(1, n_workers)]
		ranges.insert(0, (M, M+d))
		results = executor.map(S, ranges)

	t = time.time()-start
	print(sum(results))
	print("Finished in:", t)


if __name__ == '__main__':
	main()
