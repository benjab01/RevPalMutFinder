def checkWindow():

	#checks to confirm window and RF are valid
	window = input("Please enter an even-numbered RE recognition length: ")
	while (window % 2)!= 0 :
		window = input("Please enter an even numbered window: ") ;
		while window > 8 or window < 4:
			window = input("Window must be between 4 and 8 bps in length: ");
	return window

