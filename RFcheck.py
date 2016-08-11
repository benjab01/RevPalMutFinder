def RFcheck(RF):
	while (RF<1 or RF>3):
		RF = raw_input("Please enter a valid reading frame ");
		print RF;
	print "success!"
