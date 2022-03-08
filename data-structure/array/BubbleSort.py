# Time complexity- O(n^2)
# Space complexity- O(1)
def bubbleSort(a):
    for i in range(len(a) - 1, 0, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


a = [3, 2, 123, 6, 7, 5, 1, 2, -9, 100]
bubbleSort(a)
print(a)
