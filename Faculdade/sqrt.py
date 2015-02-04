import math


precisao = 1e-8

def equacao(n, x):
	return x*x - n

def eqDerivada(x):
	return 2*x

def phi(n, x):
	return x - equacao(n, x)/eqDerivada(x)


def newtonRaphson(n, x):

	if x < 0:
		return (-1, 0)
	elif x == 0:
		return (0, 0)

	
	its = 0
	while(abs(equacao(n, x)) > precisao):
		x = phi(n, x)
		its += 1

	
	return (x, its)



def bissecao(x, a, b):

	if x < 0:
		return (-1, 0)
	elif x == 0:
		return (0, 0)
	
	ini, meio, fim = a, (a+b)/2.0, b
	its = 0
	
	while(abs(fim-ini) > precisao):
		meio = (ini+fim)/2.0
		if(meio*meio > x):
			fim = meio
		else:
			ini = meio
		its += 1
	
	return (meio, its)



if __name__ == "__main__":
	while(True):
		print("Digite o valor da raiz quadrada e o chute inicial: ")
		n, x0 = map(float, input().split())
		res = bissecao(n, x0, n)
		print("Bissecao resultado: %.8lf" % res[0])
		print("Bissecao iteracoes: %d" % res[1])

		res = newtonRaphson(n, x0)
		print("Newton-Raphson resultado: %.8lf" % res[0])
		print("Newton-Raphson iteracoes: %d" % res[1])
