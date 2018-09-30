z = int(input("Enter value x: "))


def value_even(x):
	
	if x == None or x == 0:
		print( "Value x = 0 or not enter! ")
	elif x % 2 == 0:
		print( "Value x even. ")
	else:
		print( "Value x not even. ")
		
	      
value_even(z)