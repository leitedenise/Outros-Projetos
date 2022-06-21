'2- Fibonacci:'

A=[0,1]
n = int(input("Informe um número: "))
for i in range(2,20):
    A.append(A[i-1]+A[i-2])
print('\n20 primeiros valores da série de fibonacci: \n', A)

if n in A:
    print(f"\nO número {n} pertence à sequência de Fibonacci.")
else:
    print(f"\nO número {n} não pertence à sequência de Fibonacci.")