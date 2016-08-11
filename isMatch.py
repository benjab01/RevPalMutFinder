def isMatch(orderedPair) :
	pos1 = orderedPair[0]
	pos2 = orderedPair[1]
	if(pos1)=='A':
		if pos2=='T':
			return True
		else:
			return False

	if(pos1)=='T':
		if pos2=='A':
			return True
		else:
			return False

	if(pos1)=='G':
		if pos2=='C':
			return True
		else:
			return False

	if(pos1)=='C':
		if pos2=='G':
			return True
		else:
			return False