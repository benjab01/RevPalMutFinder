from isMatch import isMatch
from revpalcheck import revpalcheck
from switch import switch
def mutate(goodrevpal):
	#mut1 = ''
	#mut2 = ''
	potrevpal = goodrevpal[:]
	window = len(goodrevpal)
	mutPair = []
	count = 0
	orderedPair = []

	#print goodrevpal
	for i in potrevpal:
		orderedPair = [potrevpal[count], potrevpal[window-count-1]]
	#	orderedPair = [i, potrevpal[window-count-1]]
		if isMatch(orderedPair) != True:
	#		if count < (window/2-1):
			i = switch(potrevpal[window-count-1])
	#		potrevpal[count] = i
			potrevpal[window-count-1] = switch(potrevpal[count])
			#print count
			mutPair.append(potrevpal)
			potrevpal = goodrevpal[:]
		count = count+1
	#print 'Mutpair is ', mutPair
	return mutPair