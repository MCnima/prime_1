import sys


def main():
    number = int(sys.argv[1])
    factor_counter = 0
    for factor in range(1, number+1):
        if number % factor == 0:
            factor_counter += 1
    if factor_counter == 2:
        print('Number is prime')
    else:
        print('Number is NOT prime')


if __name__ == '__main__':
    main()
