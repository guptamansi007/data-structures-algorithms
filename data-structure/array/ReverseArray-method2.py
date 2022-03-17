def revArr(a):
    n = len(a)

    for i in range(0,int(n/2)):
        temp = a[i]
        a[i] = a[n-1-i]
        a[n - 1 - i] = temp
    print(a)

a = [7,5,6,8]
revArr(a)

