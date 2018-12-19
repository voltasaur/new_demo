import math
import cmath


def func_sin(x):
	a = (1 - math.sin(x)**2)**0.5
	return a

def func_ger(a,b,c):
	p = (a+b+c)/2
	s = (p*(p-a)*(p-b)*(p-c))**0.5
	return s

if __name__ == "__main__":
	a = float(input("Введите значение а: "))
	b = float(input("Введите значение b: "))
	c = float(input("Введите значение c: "))
	print(func_ger(a,b,c))

print("digit PI = " + str(round(math.pi,2)))