from isMatch import isMatch
from translate import translate
#from initialize import initialize
from revpalcheck import revpalcheck
from mutate import mutate
def searchUTR(window, newSeq):
	iters = len(newSeq)-window
	potrevpal = ['a']*window
	revpallist = [];
	#initialConditions = initialize(RF, newSeq)
	mut0 = []
	mut1 = []
	mutPair = []
	for i in range(0,iters):
		potrevpal = newSeq[i:i+window]
		if revpalcheck(potrevpal) :
			mutPair = mutate(potrevpal)
			mut0 = mutPair[0]
			mut1 = mutPair[1]
			ID = [i+1, potrevpal, ' ---->',mut0]
			revpallist.append(ID)
			ID = [i+1, potrevpal, ' ---->',mut1]
			revpallist.append(ID)
	return revpallist