INF = float("inf")


# O(n^2)
def find_maximum_subarray_bruteforce(A):
	n = len(A)
	max_sum = (0, 0, -INF)
	for i in range(n):
		for j in range(i+1, n):
			aux = sum(A[i:j]) # sum [i,j)
			if aux > max_sum[2]:
				max_sum = (i, j-1, aux)
	return max_sum



# O(n) -> Adaptacao de Kadane's Algorithm
def find_maximum_subarray_linear(A):
	n = len(A)
	max_sum = [0, 0, A[0]]
	max_aux = A[0]

	for i in range(1, n):
		if max_aux+A[i] > A[i]:
			max_aux += A[i]
		else:
			max_aux = A[i]
			max_sum[0] = i

		if max_aux > max_sum[2]:
			max_sum[1] = i
			max_sum[2] = max_aux


	return max_sum



def find_maximum_cross_subarray(A, p, q ,r):
	
	left_sum = -INF
	left_max = 0
	s = 0

	for i in range(q, p-1, -1):
		s += A[i]
		if s > left_sum:
			left_sum = s
			left_max = i


	right_sum = -INF
	right_max = 0
	s = 0

	for i in range(q+1, r):
		s += A[i]
		if s > right_sum:
			right_sum = s
			right_max = i

	return [left_max, right_max, left_sum+right_sum]




# O(nlgn)
def find_maximum_subarray_divconq(A, p, r):
	if p == r:
		return [p, r, A[r]]
	else:
		m = int((p+r)/2)

		lp, lr, ls = find_maximum_subarray_divconq(A, p, m)
		rp, rr, rs = find_maximum_subarray_divconq(A, m+1, r)
		cp, cr, cs = find_maximum_cross_subarray(A, p, m, r)

		if ls > rs and ls > cs:
			return [lp, lr, ls]
		elif rs > ls and rs > cs:
			return [rp, rr, rs]

		return [cp, cr, cs]



A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

x = find_maximum_subarray_bruteforce(A)
print(x)

x = find_maximum_subarray_linear(A)
print(x)

x = find_maximum_subarray_divconq(A, 0, len(A)-1)
print(x)
