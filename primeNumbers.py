def isPrime(number):
    counter = 0
    for i in range(1, number + 1):
        if(i == 1 or i == number):
            continue
        if(number % i == 0):
            counter += 1
    if(counter == 0):
        return True
    else:
        return False


def main():
    number = int(input('write number: '))
    if(not(isPrime(number)) or number == 1):
        print('no prime')
    else:
        print('is prime')


if __name__ == "__main__":
    main()
