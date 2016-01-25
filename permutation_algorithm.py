import time

# we can call this functions, but it is less efficient ~ 46 sec
def get_permutations(letters):
	if len(letters) == 0:
		return []
	elif len(letters) == 1:
		return [letters]
	else:
		words = []
		for i in range(len(letters)):
			x = letters[i]
			xs = letters[:i] + letters[i+1:]
			#print("x:%s   xs:%s" % (x,xs))
			for p in permutate(xs):
				result = x + p
				if result not in words:
					words.append(result)
		return words

# or this, ~ 40 sec
def get_permutations_updated(word):
	words = []
	for permutation in permutate(word):
		if permutation not in words:
			words.append(permutation)
	
	return words
		
def permutate(letters):
	if len(letters) == 0:
		yield []
	elif len(letters) == 1:
		yield letters
	else:
		for i in range(len(letters)):
			x = letters[i]
			xs = letters[:i] + letters[i+1:]
			# !NOTE that if I will call the same method, it will be same execution time!
			for p in get_permutations(xs):
				yield x + p

		

word = "abandoned"

algorithm1_start = time.time()

algorithm1_all = get_permutations(word)

algorithm1_end = time.time()

algorithm1_time = int(algorithm1_end - algorithm1_start)


algorithm2_start = time.time()

algorithm2_all = get_permutations_updated(word)

algorithm2_end = time.time()

algorithm2_time = int(algorithm2_end - algorithm2_start)


print("There are %d anagrams of %s. Time: %s sec using original algorithm" % (len(algorithm1_all), word, algorithm1_time))
print("There are %d anagrams of %s. Time: %s sec using updated algorithm" % (len(algorithm2_all), word, algorithm2_time))

#for p in all:
#	print("%s" % (p))