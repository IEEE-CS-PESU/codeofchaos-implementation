
import math

def isPerfectSquare(x):
	s = int(math.sqrt(x))
	return s+s == x # s*s changed to s+s


def isFibonacci(n):
  
	return isPerfectSquare(4*n*n + 4) or isPerfectSquare(4*n*n - 4) # 5*n*n changed to 4*n*n in both occurrences 
	

for i in range(1,11):
	if (isFibonacci(i) == False): # 'True' changed to 'False'
		print (i,"is a Fibonacci Number")
	else:
		print (i,"is a not Fibonacci Number ")
