def insertion_sort(A):
	for j in range(1, len(A)):
		
		chave = A[j]
		i = j-1
		
		while i >= 0 and A[i] > chave:
			A[i+1] = A[i]
			i -= 1

		A[i+1] = chave
	
	return A


def insertion_sort_reverse(A):
	for j in range(1, len(A)):
		
		chave = A[j]
		i = j-1
		
		while i >= 0 and A[i] < chave:
			A[i+1] = A[i]
			i -= 1

		A[i+1] = chave
	
	return A


def busca_linear(A, v):
	for i in range(len(A)):
		if A[i] == v:
			return i
	return None


def soma_de_binarios(A, B):

	n = len(A)
	C = [0 for i in range(n+1)]
	
	for i in range(n, 0, -1):

		soma = C[i] + A[i-1] + B[i-1]
		C[i] = soma%2
		C[i-1] = int(soma/2)

	return C


A = [31,41,59,26,41,58]

print(insertion_sort(A))
print(insertion_sort_reverse(A))

print(busca_linear(A, 31))

print(soma_de_binarios([1,0,0], [0,1,1]))
