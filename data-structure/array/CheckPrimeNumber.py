def checkPrime(num):

#Time complexity= O(n)
#Space complexity= O(1)
    if (num < 2):
        print(num," is Non Prime Num")
        return

    isPrime = True
    for i in range(2, int(num/2 + 1)):
        if (num%i == 0):
            isPrime = False

    if (isPrime):
        print(num," is Prime Num")
    else:
        print(num," is Non Prime Num")

def driver():
    num = -8
    checkPrime(num)

driver()
