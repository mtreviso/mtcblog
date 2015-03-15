# Ref:
# http://en.wikipedia.org/wiki/Approximations_of_%CF%80

from math import pi, sqrt, atan

def pi_archimedes(n):
	
	pe = 2.0
	ps = 4
	for i in range(n):
		pe = 2 - 2*sqrt(1 - pe/4)
		ps *= 2

	return ps * sqrt(pe)/2


def pi_leibniz(n):
	total = 1
	minus = True
	den = 3

	for i in range(n):
		if minus:
			total -= 1.0/den
		else:
			total += 1.0/den

		den += 2
		minus = not minus

	return total * 4



def pi_machinlike(n):
	return 4*(4*atan(1/5.0) - atan(1/239.0))



def pi_liuhui(n):
	s = sqrt(2 + 1)
	for i in range(n):
		s = sqrt(2 + s)
	return 768 * sqrt(2 - s)


def pi_madhava(n):
	
	s = 0
	for i in range(n):
		r = (1.0 /((2*i + 1) * 3**i))
		if i % 2 == 0:
			s += r
		else:
			s -= r
	return sqrt(12)*s


def pi_euler(n):
	return 20*atan(1/7.0) + 8*atan(3/79.0)



def pi_newton(n):

	s = 1 + n/(2*n + 1)
	for i in range(n, 0, -1):
		s = 1 + (i/(2*i + 1))*s
	return 2*s



def pi_takano(n):
	return 4*(12*atan(1.0/49) + 32*atan(1.0/57) - 5*atan(1.0/239) + 12*atan(1.0/110443))



def pi_stormer(n):
	return 4*(44*atan(1.0/57) + 7*atan(1.0/239) - 12*atan(1.0/682) + 24*atan(1.0/12943))



def test(name, fun, n, debug=False):

	print("\n%s:" % name)
	
	if debug:
		print("-"*25)
		print("\nIter: \t PI Value: \t Error:")
	
	if debug:
		for i in range(n):
			res = fun(i)
			err = abs(pi-res)
			print("%d \t %.10f \t %.10f" %(i, res, err))
	else:
		res = fun(n)
		print("%.20f" % res, end="")
		print("\t", end="")
		print(abs(pi-res))





if __name__ == "__main__":
	
	print("PI:", pi)
	
	test("Leibniz", pi_leibniz, 1000000)
	test("Archimedes", pi_archimedes, 16)
	test("Machin-like", pi_machinlike, 1)
	test("Liu Hui", pi_liuhui, 7)
	test("Madhava", pi_madhava, 100)
	test("Euler", pi_euler, 1)
	test("Newton", pi_newton, 48)
	test("Takano", pi_takano, 1)
	test("Stormer", pi_stormer, 1)

