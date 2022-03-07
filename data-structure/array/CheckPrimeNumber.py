def checkPrime(num):
# Time complexity = n
# space complexity = 1
    isPrime = 1
    if num > 1:
        for i in range(2, int(num/2 + 1)):
            if (num%i == 0):
                isPrime = 0;
                print(num, "is not a prime number")
                break

        if(isPrime == 1):
            print(num, "is a prime number")


def driver():
    num = 30
    checkPrime(num)

driver()
