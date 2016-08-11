from isMatch import isMatch
from translate import translate
#from initialize import initialize
from revpalcheck import revpalcheck
from mutate import mutate
from triPepTrans import triPepTrans
from checkRF import checkRF
from checkWindow import checkWindow
def search(RF, window, newSeq):

	iters = len(newSeq)-window
	potrevpal = ['a']*window
	revpallist = [];
	#initialConditions = initialize(RF, newSeq)
	mut0 = []
	mut1 = []
	mutPair = []
	#Locus = 0
	mutSeq0 = newSeq[:]
	mutSeq1 = newSeq[:]


	ID = ['X', 'X']
	#print triPepTrans(9,1,newSeq)
	#print newSeq[8]


	for i in range(0,iters):
		potrevpal = newSeq[i:i+window]
		if revpalcheck(potrevpal) :
			#print 'mutSeq0 is ', mutSeq0, 
			#print 'mutSeq1 is ', mutSeq1 
			#print 'newSeq is ', newSeq
			mutPair = mutate(potrevpal)
			mut0 = mutPair[0]
			mut1 = mutPair[1]	
			mutSeq0[i:i+window] = mut0
			#print mutSeq0
			mutSeq1[i:i+window] = mut1
			#print mutSeq1
			print 'i = ' , i
			print triPepTrans(i, RF, newSeq), ' = wtTrans'
			print triPepTrans(i,RF,mutSeq0), ' = mutTrans0'
			print triPepTrans(i,RF,mutSeq1), ' = mutTrans1'
			if triPepTrans(i,RF,newSeq):
				if triPepTrans(i,RF,mutSeq0) == triPepTrans(i, RF, newSeq) :
					ID = [i, potrevpal,' ---->',mut0]
					revpallist.append(ID)
					#print triPepTrans(i,RF,mutSeq0)
					#print triPepTrans(i,RF,newSeq)
				if triPepTrans(i,RF,mutSeq1) == triPepTrans(i, RF, newSeq) :
					ID = [i,potrevpal, ' ---->',mut1]
					revpallist.append(ID)
					#print triPepTrans(i,RF,mutSeq1)
					#print triPepTrans(i,RF,newSeq)				
			mutSeq0 = newSeq[:]
			mutSeq1 = newSeq[:]

	return revpallist
