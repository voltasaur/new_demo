
print (" Calculation of the mass of the human body. ")

mass_body = float(input(" Enter your mass : "))
growth = float(input(" Enter your growth : "))

vall = growth / 100 
bmi = round (mass_body / (vall**2),2)

if bmi < 16:
	print (" Pronounced deficit of body weight : " + str(bmi))
elif bmi >= 16 and bmi < 18.5:
	print (" Deficit of body weight : " + str(bmi))
elif bmi >= 18.5 and bmi < 24.99:
	print (" Normal body weight : " + str(bmi))
elif bmi >= 25 and bmi < 30:
	print (" Excess body weight : " + str(bmi))
elif bmi >= 30 and bmi < 35:
	print (" Obesity body weight : " + str(bmi))
elif bmi >= 35 and bmi < 40:
	print (" Obesity is sharp : " + str(bmi))
elif bmi > 40:
	print (" Very severe obesity : " + str(bmi))
else :
	print (" Error value : " + str(bmi))


"""
16 и менее	Выраженный дефицит массы тела
16—18,5	Недостаточная (дефицит) масса тела
18,5—24,99	Норма
25—30	Избыточная масса тела (предожирение)
30—35	Ожирение
35—40	Ожирение резкое
40 и более	Очень резкое ожирение
"""
