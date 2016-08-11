from isMatch import isMatch
from translate import translate
#from initialize import initialize
from revpalcheck import revpalcheck
from mutate import mutate
from triPepTrans import triPepTrans
from checkRF import checkRF
from checkWindow import checkWindow
from search import search
from isUTR import isUTR
from searchUTR import searchUTR

f = open('Sequence.txt','r');
seq = f.read();
#seq = seq.split('\n')


newSeq = list(seq);

#convert lowercases to uppercases
upperSeq = []
for x in newSeq:
	upperSeq.append(x.upper())
#print upperSeq
#converts sequence into a list of separate 1-character strings

#generate valid input and window
window = checkWindow()
status = raw_input("Does cut occur in gene? Enter 'UTR' or 'ORF': ")
if isUTR(status):
	RF = checkRF()
	print search(RF, window, upperSeq)
else:
	print searchUTR(window, upperSeq)

