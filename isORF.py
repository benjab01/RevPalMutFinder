def isORF(status):
	lim = True
	while lim:
		if status == 'UTR':
			lim = False
			return False
		elif status == 'ORF':
			lim = False
			return True
		else:
			status = raw_input("Invalid entry. Enter 'UTR' or 'ORF'): ")
