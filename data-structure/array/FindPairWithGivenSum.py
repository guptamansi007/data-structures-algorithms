# Given an array A[] and a number x, check for pair in A[] with sum as x (aka Two Sum)

# Time complexity : O(NlogN)
# Space complexity : O(1)
def findPair(a, x):
    a.sort()
    low_index = 0
    high_index = len(a) - 1

    isExist = False
    while low_index < high_index:
        if a[low_index] + a[high_index] == x:
            print("valid pair exists", a[low_index], a[high_index])
            isExist = True
            break
        elif a[low_index] + a[high_index] < x:
            low_index = low_index + 1
        else:
            high_index = high_index - 1

    if (isExist == False):
        print("Pair doesn't exit")


a = [1, 2, 4, 7, 9, 10, 5]
x = 9
findPair(a, x)
