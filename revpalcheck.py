from isMatch import isMatch
def revpalcheck(query) :
	#query = ['A', 'T', 'G', 'C', 'A', 'A']
	queryPair = ['S','S']
	matchCount = 0
	window = len(query)
	#i=0
	for i in range(0, window/2) :
		queryPair = [query[i], query[(window-i-1)]]
		if isMatch(queryPair):
			matchCount = matchCount +1
	if matchCount==((window/2)-1):
		return True
		#print "True"
	else:
		return False
		#print "False"