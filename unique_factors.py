##
# Write a script to compute how many unique prime factors an integer has.
# For example, 12 = 2 x 2 x 3, so has two unique prime factors, 2 and 3. Use your script to compute the number of unique prime factors of 1234567890.
# author: marquis103
# assignment: MIDS Data Structures and Algorithms assignment
#

factors = set()
primeFactors = set()
baseNumber = int(input('Enter a number to calculate how many unique prime factors exist for the integer: '))

# get factors 
for n in range(2, baseNumber):
	if baseNumber % n == 0:
		factors.add(n)

#determine if the factors are prime
if len(factors) > 0:
	for factor in factors:
		primeCounter = 1
		
		while primeCounter < factor:
			if (factor % primeCounter == 0) and (primeCounter > 1):
				break
			if (factor - primeCounter) == 1:
				primeFactors.add(factor)
			primeCounter += 1

	if len(primeFactors) > 0:
		print (primeFactors)
	else:
		print('This number does not have any prime factors')			
else:
	print('This number does not have any factors')