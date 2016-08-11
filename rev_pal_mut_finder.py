from isMatch import isMatch
from translate import translate
from initialize import initialize
from revpalcheck import revpalcheck
from mutate import mutate
from triPepTrans import triPepTrans
f = open('Sequence.txt','r');
seq = f.read();
#seq = seq.split('\n')

newSeq = list(seq);
#print newSeq
#converts sequence into a list of separate 1-character strings

#checks to confirm window and RF are valid
window = input("Please enter an even-numbered RE recognition length: ")
while (window % 2)!= 0 :
	window = input("Please enter an even numbered window: ") ;
	while window > 8 or window < 4:
		window = input("Window must be between 4 and 8 bps in length: ");


RF=input("Please enter a valid reading frame (0, 1, or 2) ")
while (RF<0 or RF>2):
	#print "while loop entered, RF = " , RF
	RF=input("Please enter a valid reading frame (0, 1, or 2) ");
	#print RF;
#print "success!"


#seqIndex = 0;
iters = len(newSeq)-window
potrevpal = ['a']*window
revpallist = [];
#initialConditions = initialize(RF, newSeq)
mut0 = []
mut1 = []
mutPair = []
#Locus = 0
mutSeq0 = []
mutSeq1 = []


ID = ['X', 'X']

for i in range(0,iters):
	potrevpal = newSeq[i:i+window]
	if revpalcheck(potrevpal) :
		mutPair = mutate(potrevpal)
		mut0 = mutPair[0]
		mut1 = mutPair[1]	
		mutSeq0[i:i+window] = mut0
		mutSeq1[i:i+window] = mut1
		if triPepTrans(i,RF,mutSeq0) == triPepTrans(i, RF, newSeq) :
			ID = [i, mut0]
			revpallist.append(ID)
		if triPepTrans(i,RF,mutSeq1) == triPepTrans(i, RF, newSeq) :
			ID = [i+1, mut1]
			revpallist.append(ID)
			#'\n'.join(''.join(revpallist))
print revpallist
