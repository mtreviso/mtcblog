def merge(A, p, q, r):

	n1 = q-p+1
	n2 = r-q

	L = [A[p+i] for i in range(n1)]
	R = [A[q+i+1] for i in range(n2)]

	i,j = 0,0
	for k in range(p, r+1):
		if j >= n2 or (i < n1 and L[i] <= R[j]):
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1

	return A


def merge_sort(A, p, r):
	if p < r:
		q = int((p+r)/2)
		merge_sort(A, p, q)
		merge_sort(A, q+1, r)
		merge(A, p, q, r)
	return A


def busca_binaria(A, p, r, v):
	if p <= r:
		q = int((p+r)/2)
		if A[q] > v:
			return busca_binaria(A, p, q-1, v)
		elif A[q] < v:
			return busca_binaria(A, q+1, r, v)
		else:
			return q
	return -1


def soma_de_dois_inteiros(A, x):
	
	n = len(A)
	for i in range(n):
		x1 = A[i]
		j = busca_binaria(A, 0, n, x-x1)
		if j >= 0:
			x2 = A[j]
			return (x1, x2)

	return None




A = [3, 41, 52, 26, 38, 59, 7, 41]
print(merge_sort(A, 0, 7))
print(busca_binaria(A, 0, 7, 26))
print(soma_de_dois_inteiros(A, 49))
