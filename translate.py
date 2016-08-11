def translate(codon):
#codon = ['C', 'A', 'A']
	pep = 'X'
	if codon[0] == 'T':
		if codon[1] == 'T':
			if codon[2] == 'T' or codon[2] == 'C':
				pep = 'F'
			else:
				pep = 'L'
		elif codon[1] == 'C':
			pep = 'S'
		elif codon[1] == 'A':	
			if codon[2] == 'T' or codon[2] == 'C':
				pep = 'Y'
			else:
				pep = '*'
		elif codon[1] == 'G':
			if codon[2] == 'T' or codon[2] == 'C':
				pep = 'C'
			elif codon[2] == 'A':
				pep = '*'	
			else:
				pep = 'W'

	elif codon[0] == 'C':
		if codon[1] == 'T':
			pep = 'L'
		elif codon[1] == 'C':
			pep = 'P'
		elif codon[1] == 'A':	
			if codon[2] == 'T' or codon[2] == 'C':
				pep = 'H'
			else:
				pep = 'Q'			
		elif codon[1] == 'G':
			pep = 'R'

	elif codon[0] == 'A':
		if codon[1] == 'T':
			if codon[2] == 'G':
				pep = 'M'
			else:
				pep = 'I'
		elif codon[1] == 'C':
			pep = 'T'
		elif codon[1] == 'A':	
			if codon[2] == 'T' or codon[2] == 'C':
				pep = 'N'
			else:
				pep = 'K'	
		elif codon[1] == 'G':
			if codon[2] == 'T' or codon[2] == 'C':
				pep = 'S'
			else:
				pep = 'R'	

	elif codon[0] == 'G':
		if codon[1] == 'T':
			pep = 'V'
		elif codon[1] == 'C':
			pep = 'A'
		elif codon[1] == 'A':	
			if codon[2] == 'T' or codon[2] == 'C':
				pep = 'D'
			else:
				pep = 'E'	
		elif codon[1] == 'G':
			pep = 'G'	

	#print pep
	return pep

