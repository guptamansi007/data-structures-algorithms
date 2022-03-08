def bubbleSort(a):
    for i in range (len(a)-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j] , a[j+1] = a[j+1] , a[j]

a = [3,2,1,6,7,5]
bubbleSort(a)
print(a)
