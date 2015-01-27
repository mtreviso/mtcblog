from math import log, sqrt

def log2(x):
	return log(x, 2)



# calculo fatorial ate 100
fat = [1 for i in range(100)]
for i in range(2, 100):
	fat[i] = i*fat[i-1]



# constante tempo
TEMPO = 100*365*30*24*60*60*(10**6)



# helpers
def equacao(x):
	return x*log2(x) - TEMPO

def eqDerivada(x):
	return (log(x) + 1)/log(2)

def phi(x):
	return x - equacao(x)/eqDerivada(x)


def newtonRaphson(x, precisao):
	
	y = equacao(x)
	while(abs(y) > precisao):
		x = phi(x)
		y = equacao(x)

	return x


def testaRaizes():
	print(newtonRaphson(1561561, 0.1))




def eq1(x):
	return fat[x]

def eq2(x):
	return TEMPO


def test(x):
	return (eq1(x) >= eq2(x))


def testaLimite():
	for i in range(1, 100):
		if test(i):
			print(i-1)
			break




# main
testaRaizes()
print log2(TEMPO)
testaLimite()

