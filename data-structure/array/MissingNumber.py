#https://www.geeksforgeeks.org/find-the-only-missing-number-in-a-sorted-array/

def missingNumber(a):
    lower = 0
    upper = len(a) - 1

    while (lower <= upper):
        mid = (lower + upper) // 2
        if (a[mid] != mid + 1 and a[mid-1] == mid):
            return (mid +1)
        elif (a[mid] != mid + 1):
            upper = mid - 1
        else:
            lower = mid + 1

    return False

a = [1,2,3,5,6,7,8,9]
print(missingNumber(a))













