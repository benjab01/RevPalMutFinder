from isMatch import isMatch
from translate import translate
from initialize import initialize
from triPepTrans import triPepTrans
from switch import switch
from mutate import mutate
from revpalcheck import revpalcheck
from isUTR import isUTR
from searchUTR import searchUTR

#RF=input("Please enter a valid reading frame ")
#while (RF<1 or RF>3):
	#print "while loop entered, RF = " , RF
#	RF=input("Please enter a valid reading frame ");
	#print RF;
#print "success!"

#count = 0
#while (count < 10):
#	print "The count is ", count
#	count = count + 1
#

# #window = 9
# #while window > 8 :
# #	window = input("Window must be fewer than 8 bps in length: ");
# window = input("Please enter an even-numbered RE recognition length: ")
# while (window % 2)!= 0 :
# 	window = input("Please enter an even numbered window: ") ;
# 	while window > 8 or window < 4:
# 		window = input("Window must be between 4 and 8 bps in length: ");


# RF=input("Please enter a valid reading frame (1, 2, or 3) ")
# while (RF<1 or RF>3):
# 	#print "while loop entered, RF = " , RF
# 	RF=input("Please enter a valid reading frame (1, 2, or 3) ");
# 	#print RF;
# #print "success!"

# orderedPair = ['G','G']
# pos1 = orderedPair[0]
# pos2 = orderedPair[1]
# if(pos1)=='A':
# 	if pos2=='T':
# 		print 1
# 		#return True
# 	else :
# 		print 2
# 		#return False

# if(pos1)=='T':
# 	if pos2=='A':
# 		print 3
# 		#return True
# 	else :
# 		print 4
# 		#return False

# if(pos1)=='G':
# 	if pos2=='C':
# 		print 5
# 		#return True
# 	else :
# 		print 6
# 		#return False

# if(pos1)=='C':
# 	if pos2=='G':
# 		print 7
# 		#return True
# 	else :
# 		print 8
# 		#return False

# query = ['A', 'C', 'C', 'C', 'G', 'C', 'A','T']
# queryPair = ['S','S']
# matchCount = 0
# window = len(query)
# i=0
# for i in range(0, (window/2)-1) :
# 	queryPair = [query[i], query[(window-i-1)]]
# 	if isMatch(queryPair):
# 		matchCount = matchCount +1
# if matchCount==((window/2)-1):
# 	#return True
# 	print "True"
# else:
# 	#return False
# 	print "False"

# codon = ['C', 'A', 'A']
# pep = 'X'
# if codon[0] == 'T':
# 	if codon[1] == 'T':
# 		if codon[2] == 'T' or codon[2] == 'C':
# 			pep = 'F'
# 		else:
# 			pep = 'L'
# 	elif codon[1] == 'C':
# 		pep = 'S'
# 	elif codon[1] == 'A':	
# 		if codon[2] == 'T' or codon[2] == 'C':
# 			pep = 'Y'
# 		else:
# 			pep = '*'
# 	elif codon[1] == 'G':
# 		if codon[2] == 'T' or codon[2] == 'C':
# 			pep = 'C'
# 		elif codon[2] == 'A':
# 			pep = '*'	
# 		else:
# 			pep = 'W'

# elif codon[0] == 'C':
# 	if codon[1] == 'T':
# 		pep = 'L'
# 	elif codon[1] == 'C':
# 		pep = 'P'
# 	elif codon[1] == 'A':	
# 		if codon[2] == 'T' or codon[2] == 'C':
# 			pep = 'H'
# 		else:
# 			pep = 'Q'			
# 	elif codon[1] == 'G':
# 		pep = 'R'

# elif codon[0] == 'A':
# 	if codon[1] == 'T':
# 		if codon[2] == 'G':
# 			pep = 'M'
# 		else:
# 			pep = 'I'
# 	elif codon[1] == 'C':
# 		pep = 'T'
# 	elif codon[1] == 'A':	
# 		if codon[2] == 'T' or codon[2] == 'C':
# 			pep = 'N'
# 		else:
# 			pep = 'K'	
# 	elif codon[1] == 'G':
# 		if codon[2] == 'T' or codon[2] == 'C':
# 			pep = 'S'
# 		else:
# 			pep = 'R'	

# elif codon[0] == 'G':
# 	if codon[1] == 'T':
# 		pep = 'V'
# 	elif codon[1] == 'C':
# 		pep = 'A'
# 	elif codon[1] == 'A':	
# 		if codon[2] == 'T' or codon[2] == 'C':
# 			pep = 'D'
# 		else:
# 			pep = 'E'	
# 	elif codon[1] == 'G':
# 		pep = 'G'	

# print pep

# seq = 'ATGGAGTGGTAGCTCCATGTCGAGCCCTCAGTCTACGTACTACGT'
# newSeq = list(seq)
# codon = ['X', 'X', 'X']
# codonList = []
# codonIter = 0;
# initialTrans = []
# RF = 0
# #generate codons
# for x in range(RF,len(newSeq)):
# 	codon[codonIter] = newSeq[x]
# 	codonIter = codonIter + 1
# 	if codonIter%3 == 0:
# 		codonIter = 0
# 		codonList.append(codon)
# 		codon = ['X', 'X', 'X']

# #translate codons
# for y in range(0,len(codonList)):
# 	initialTrans.append(translate(codonList[y]))

# #return initialTrans
# print initialTrans



# Trans = initialize(0, newSeq)
# print Trans

# loc = 1
# codonList = []
# codonIter = 0;
# codon = ['X', 'X', 'X']
# local = loc
# #tripep = [pep1, pep2, pep3]

# #check to make sure you are not looking outside of range
# RF = 0



# if RF!=1:
# 	if loc < 2:
# 		#return False
# 		print 'False'
# else:
# 	if loc > (len(newSeq)-3) :
# 		#return False
# 		print 'False'


# if loc%3==RF:
# 	for x in range(0, 9):
# 		codon[codonIter] = newSeq[local+x]
# 		codonIter = codonIter + 1
# 		if codonIter%3 == 0:
# 			codonIter = 0
# 			codonList.append(codon)
# 			codon = ['X', 'X', 'X']
# elif (loc%3 -1) == RF:
# 	for x in range(0,9):
# 		codon[codonIter] = newSeq[local+x-1]
# 		codonIter = codonIter +1
# 		if codonIter%3 == 0:
# 			codonIter = 0
# 			codonList.append(codon)
# 			codon = ['X', 'X', 'X']
# else:
# 	for x in range(0,9):
# 		codon[codonIter] = newSeq[local+x-2]
# 		codonIter = codonIter +1
# 		if codonIter%3 == 0:
# 			codonIter = 0
# 			codonList.append(codon)
# 			codon = ['X', 'X', 'X']

# print codonList
# triPep = []
# for n in codonList:
# 	triPep.append(translate(n))
# print triPep

#print triPepTrans(6,2,newSeq)

#goodrevpal = ['A','C','T','G','C','A','C','T']
# potrevpal = goodrevpal[:]
# window = len(goodrevpal)
# mutPair = []
# count = 0
# orderedPair = []

# print goodrevpal
# for i in potrevpal:
# 	orderedPair = [potrevpal[count], potrevpal[window-count-1]]
# #	orderedPair = [i, potrevpal[window-count-1]]
# 	if isMatch(orderedPair) != True:
# #		if count < (window/2-1):
# 		i = switch(potrevpal[window-count-1])
# #		potrevpal[count] = i
# 		potrevpal[count] = switch(potrevpal[window-count-1])
# 		#print count
# 		mutPair.append(potrevpal)
# 		potrevpal = goodrevpal
		#print 'goodrevpal is ',goodrevpal
		#print potrevpal
	#else:
		#potrevpal[window-count-1] = switch(potrevpal[count])
		#mutPair.append(potrevpal)
		# if potrevpal[window-count] == 'A':
		# 	potrevpal[count] = 'T'
		# elif potrevpal[window-count] == 'T':
		# 	potrevpal[count] = 'A'
		# elif potrevpal[window-count] == 'C':
		# 	potrevpal[count] = 'G'
		# else :
		# 	potrevpal[count] = 'C'
		#mutPair.append(potrevpal)
		#potrevpal = goodrevpal

		#potrevpal[window-count] = switch(potrevpal[count])

		# if potrevpal[count] == 'A':
		# 	potrevpal[window-count] = 'T'
		# elif potrevpal[count] == 'T':
		# 	potrevpal[window-count] = 'A'
		# elif potrevpal[count] == 'C':
		# 	potrevpal[window-count] = 'G'
		# else :
		# 	potrevpal[window-count] = 'C'
		#mutPair.append(potrevpal)
#	count = count+1
#print 'Mutpair is ', mutPair
#mutPair = mutate(goodrevpal)
#mut1 = mutPair[0]
#mut2 = mutPair[1]
#print mutate(goodrevpal)
#print 'mutSeq1 is ', mut1
#print 'mutSeq2 is ', mut2
seq = 'CTATCCTAGCCCCGTGATGTGACCAACTTCACCGTG'
newSeq = list(seq)
window = 6
#RF=input("Please enter a valid reading frame (0, 1, or 2) ")
# RF = 2
# iters = len(newSeq)-window
# potrevpal = ['a']*window
# revpallist = [];
# #initialConditions = initialize(RF, newSeq)
# mut0 = []
# mut1 = []
# mutPair = []
# #Locus = 0
# mutSeq0 = newSeq[:]
# mutSeq1 = newSeq[:]


# ID = ['X', 'X']


#print triPepTrans(9,1,newSeq)
#print newSeq[8]

# for i in range(0,iters):
# 	potrevpal = newSeq[i:i+window]
# 	if revpalcheck(potrevpal) :
# 		#print 'mutSeq0 is ', mutSeq0, 
# 		#print 'mutSeq1 is ', mutSeq1 
# 		#print 'newSeq is ', newSeq
# 		mutPair = mutate(potrevpal)
# 		mut0 = mutPair[0]
# 		mut1 = mutPair[1]	
# 		mutSeq0[i:i+window] = mut0
# 		#print mutSeq0
# 		mutSeq1[i:i+window] = mut1
# 		#print mutSeq1
# 		print 'i = ' , i
# 		print triPepTrans(i,RF,mutSeq0), ' = mutTrans0'
# 		print triPepTrans(i,RF,mutSeq1), ' = mutTrans1'
# 		print triPepTrans(i, RF, newSeq), ' = wtTrans'
# 		if triPepTrans(i,RF,mutSeq0) == triPepTrans(i, RF, newSeq) :
# 			ID = [i+1, mut0]
# 			revpallist.append(ID)
# 			print triPepTrans(i,RF,mutSeq0)
# 			print triPepTrans(i,RF,newSeq)
# 		if triPepTrans(i,RF,mutSeq1) == triPepTrans(i, RF, newSeq) :
# 			ID = [i+1, mut1]
# 			revpallist.append(ID)
# 		mutSeq0 = newSeq[:]
# 		mutSeq1 = newSeq[:]

# print revpallist


# status = raw_input("Does cut occur in gene? Enter 'UTR' or 'ORF'): ")
# print isORF(status)


print searchUTR(window, newSeq)

