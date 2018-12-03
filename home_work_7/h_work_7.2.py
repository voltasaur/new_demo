x = input("Enter value x: ")
y = input("Enter value y: ")

def max_value( x, y ):
	if x > y:
		print( "max value = ",x)
	elif x < y:
		print( "max value = ",y)
	else:
		print( "value  x = y ")	  
    
max_value(x,y)