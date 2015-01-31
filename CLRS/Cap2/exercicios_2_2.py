def index_min_key(A, i, n):
	m = i
	for j in range(i+1, n):
		if A[j] < A[m]:
			m = j
	return m


def selection_sort(A):

	n = len(A)
	for i in range(n-1):
		j = index_min_key(A, i, n)
		A[i], A[j] = A[j], A[i]

	return A


print(selection_sort([12, 40, 81, 35, 57, 65]))
