def splitIntoTwo(num, n):
	return num[:n//2], num[n//2:]


def karatsubaMethod(number1, number2):
	n = max(len(number1), len(number2))
	
	if n == 1:
		return int(number1) * int(number2)
	else:
		n = n if n % 2 == 0 else n + 1
		number1, number2 = number1.zfill(n), number2.zfill(n)
		A, B = splitIntoTwo(number1, n)
		C, D = splitIntoTwo(number2, n)
		
		AC = karatsubaMethod(A, C)
		BD = karatsubaMethod(B, D)
		ADBC = karatsubaMethod(str(int(A) + int(B)), str(int(C) + int(D)))
		ADBC -= (AC + BD)

		return (AC * (10 ** n)) + (ADBC * (10 ** (n // 2))) + BD

a = 3141592653589793238462643383279502884197169399375105820974944592
b = 2718281828459045235360287471352662497757247093699959574966967627
print((a * b) == karatsubaMethod(str(a),str(b)))
