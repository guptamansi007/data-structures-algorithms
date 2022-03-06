# Python program to find the common elements in two lists
# Reference : https://www.geeksforgeeks.org/python-print-common-elements-two-lists/
class CommonElementInSortedArray:

    """
        Time complexity: O(N+M)
        Space complexity: O(1)
    """
    @staticmethod
    def find_common_elements(a, b):

        result = []
        i, j = 0, 0
        N = len(a)
        M = len(b)

        while (i < N and j < M):
            if a[i] == b[j]:
                result.append(a[i])
                i += 1
                j += 1
            elif a[i] < b[j]:
                i += 1
            else:
                j += 1

        return result


def driver():

    a = [0, 1, 3, 4, 9]
    b = [1, 3, 5, 7, 8, 9]
    print(CommonElementInSortedArray.find_common_elements(a, b))

driver()


