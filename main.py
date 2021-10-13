import sys

Number = int(sys.argv[1])
factor_counter = 0
for factor in range(1, Number+1):
    if Number % factor == 0:
        factor_counter += 1
if factor_counter == 2:
    print('Number is prime')
else:
    print('Number is NOT prime')
