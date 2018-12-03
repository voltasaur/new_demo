pH = float(input("Enter the requested pH: "))

def answer_pH(val):
	if val == 3.0 :
		print ("Apple juice.", val, "pH")
	elif val == 5.5:
		print ("Shampoo.", val, "pH")
	elif val == 9.0:
		print ("Hand soap.", val, "pH")
	else:
		print ("Enter error.")
			

answer_pH(pH)
	
