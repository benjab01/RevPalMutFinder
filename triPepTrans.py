from translate import translate
def triPepTrans(loc, RF, newSeq):
	codonList = []
	codonIter = 0;
	codon = ['X', 'X', 'X','X']
	local = loc
	#print ''
	#print 'local = ',local
	#print 'local%3 = ', local%3
	if RF!=0:
		#print 'enters RF!=0:'
		if local < 1:
			#print 'False in if loc < 1'
			return False

	if local > (len(newSeq)-11) :
		#print 'False in elif loc > (len(newSeq)-8)'
		return False

	# loop for reading triPep in RF = 0
	if local%3==RF:
		#print local, 'enters if loc%3==RF'
		for x in range(0, 12):
			codon[codonIter] = newSeq[local+x]
			codonIter = codonIter + 1
			#print 'x = ', x
			#print 'codonIter = ', codonIter
			if codonIter%3 == 0:
				codonIter = 0
				codonList.append(codon)
				codon = ['X', 'X', 'X','X']
	
	#loop for reading triPep in RF = 1
	elif (local%3 -1) == RF:
		#print local, ' enters elif (loc%3 +1) == RF:'
		for x in range(0,12):
			codon[codonIter] = newSeq[local+x-1]
			codonIter = codonIter +1
			if codonIter%3 == 0:
				codonIter = 0
				codonList.append(codon)
				codon = ['X', 'X', 'X','X']
	#loop for reading triPep in RF = 2
	else:
		#print local, ' enters else (loc%3 +2) == RF:'
		for x in range(0,12):
			codon[codonIter] = newSeq[local+x-2]
			codonIter = codonIter +1
			#print 'x = ', x
			#print 'codonIter = ', codonIter			
			if codonIter%3 == 0:
				codonIter = 0
				codonList.append(codon)
				codon = ['X', 'X', 'X','X']

	#print codonList
	triPep = []
	for n in codonList:
		triPep.append(translate(n))
	#print triPep
	return triPep



			