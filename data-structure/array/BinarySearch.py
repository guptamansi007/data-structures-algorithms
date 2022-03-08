# Time complexity = O(logN)
# Space complexity = O(1)
def binarySearch(a, num):
    lower = 0
    upper = len(a) - 1
    while (lower <= upper):
        mid = (lower + upper) // 2
        if a[mid] == num:
            return True
        elif a[mid] > num:
            upper = mid - 1
        elif a[mid] < num:
            lower = mid + 1
    return False

a = [1, 2, 5, 7, 8, 9]
num = 10

if (binarySearch(a, num)):
    print("element is found")
else:
    print("element is not found")
