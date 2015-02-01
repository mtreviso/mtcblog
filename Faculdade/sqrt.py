import math
# ver metodos disponiveis na math:
# print(dir(math))

INF = 9999999

def equacao(x):
	return x/2.0


def phi(x, y):
	return y + x/y


def newtonRaphson(x, precisao):
	
	if x < 0:
		return "complex root"
	elif x == 0:
		return 0

	its = 0
	y = 1 # chute inicial
	while(abs(y*y - x) > precisao):
		y = equacao(phi(x, y))
		its += 1

	print("Bissecao iteracoes: ", its)
	return y




def bissecao(x, a, b, max_erro):

	if x < 0:
		return "complex root"
	elif x == 0:
		return 0

	ini, meio, fim = a, 0, b
	erro = fim - ini
	its = 0
	
	while(erro > max_erro):
		
		meio = (ini+fim)/2
		resx = meio*meio
		# resa = ini*ini
		
		# if(resx*resa > 0):
		if(resx > x):
			fim = meio
		else:
			ini = meio
			
		erro = fim - ini
		its += 1

	print("Bissecao iteracoes: ", its)
	return meio


# main
precisao = 1e-12


while(True):
	print("Digite a aproximacao inicial ou `STOP` para parar:")
	aprox = input()
	if(aprox.upper() == 'STOP'):
		break
	print("Resultado: %.9lf\n" % newtonRaphson(float(aprox), precisao))
	print("Resultado: %.9lf\n" % bissecao(float(aprox), -INF, INF, precisao))