def checkRF():

	RF=input("Please enter a valid reading frame (0, 1, or 2) ")
	
	while (RF<0 or RF>2):
		#print "while loop entered, RF = " , RF
		RF=input("Please enter a valid reading frame (0, 1, or 2) ");
		#print RF;
	#print "success!"
	return RF