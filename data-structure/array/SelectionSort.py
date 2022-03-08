# Time complexity = O(n^2)
# Space complexity = O(1)
def selectionSort(a):
    for i in range(len(a)):
        min_index = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]


a = [3, 1, 6, 22, 2, 3, 9, 4]
selectionSort(a)
print(a)
