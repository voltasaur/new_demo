

print ("""\tEcaterinburg---code : 343     cost : 1min = 15p 
	Omsk-----------code : 381     cost : 1min = 18p
	Voronej------- code : 443     cost : 1min = 13p
	Yroslavl------ code : 485     cost : 1min = 11p
	""")
code = {343:15, 381:18, 443:13, 485:11,}
city_code = int(input(" Enter code city: "))
time_speak = int(input(" Enter time speak: "))

if city_code in code.keys():
	print ("Price of your conversation = " + str(time_speak*code[city_code]) + "p" )
else:
	print ("Error enter!")
		 


