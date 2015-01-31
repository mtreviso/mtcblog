def bubble_sort(A):
	
	n = len(A)
	inversions = 0

	for i in range(n):
		for j in range(n-1, i, -1):
			if A[j] < A[j-1]:
				A[j], A[j-1] = A[j-1], A[j]
				inversions += 1

	return (A, inversions)


def horner(A, x):
	total = A[0]
	n = len(A)
	for i in range(1, n):
		a = A[i]
		total += (a*(x**i))

	return total


def insertion_sort(A):

	inversions = 0
	for j in range(1, len(A)):
		
		chave = A[j]
		i = j-1
		
		while i >= 0 and A[i] > chave:
			A[i+1] = A[i]
			i -= 1
			inversions += 1

		A[i+1] = chave
	
	return (A, inversions)



def merge(A, p, q, r):

	n1 = q-p+1
	n2 = r-q

	L = [A[p+i] for i in range(n1)]
	R = [A[q+i+1] for i in range(n2)]
	L.append(float("inf"))
	R.append(float("inf"))

	i,j = 0,0
	inversions = 0
	for k in range(p, r+1):
		if L[i] <= R[j]:
			A[k] = L[i]
			i += 1
		else:
			inversions += (n1-i)
			A[k] = R[j]
			j += 1

	return (A, inversions)


def merge_sort(A, p, r):
	inversions = 0
	if p < r:
		q = int((p+r)/2)
		inversions += merge_sort(A, p, q)[1]
		inversions += merge_sort(A, q+1, r)[1]
		inversions += merge(A, p, q, r)[1]
	return (A, inversions)



A = [5, 2, 4, 6, 1, 3, 2, 6]
print(bubble_sort(A))

A = [5, 2, 4, 6, 1, 3, 2, 6]
print(insertion_sort(A))

A = [2, 8, 7, 12, 0, 4, 9, 10]
print(merge_sort(A, 0, len(A)-1))
