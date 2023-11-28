# Python3 program to find LCM of
# First N Natural Numbers.
MAX = 100000

# array to store all prime less
# than and equal to 10^6
primes = []

# utility function for
# sieve of Eratosthenes


def sieve():

	isComposite = [False]*(MAX+1)
	i = 2
	while (i * i <= MAX):
		if (isComposite[i] == False):
			j = 2
			while (j * i <= MAX):
				isComposite[i * j] = True
				j += 1
		i += 1

	# Store all prime numbers in
	# vector primes[]
	for i in range(2, MAX+1):
		if (isComposite[i] == False):
			primes.append(i)

# Function to find LCM of
# first n Natural Numbers


def LCM(n):

	lcm = 1
	i = 0
	while (i < len(primes) and primes[i] <= n):
		# Find the highest power of prime,
		# primes[i] that is less than or
		# equal to n
		pp = primes[i]
		while (pp * primes[i] <= n):
			pp = pp * primes[i]

		# multiply lcm with highest
		# power of prime[i]
		lcm *= pp
		lcm %= 1000000007
		i += 1
	return lcm


# Driver code
sieve()
N = 7

# Function call
print(LCM(N))


