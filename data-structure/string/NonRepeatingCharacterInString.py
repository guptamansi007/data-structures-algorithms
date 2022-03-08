# Find the non-repeating character in the given string
"""
   Time complexity: 0(N)
   Space complexity: O(N) -> to be verified
"""

def NonRepeating(str):

    count = {}
    result = []

    for c in str:
        if c not in count:
            count[c] = 1
        else:
            count[c] = count[c] + 1

    for c in str:
        if count[c] == 1:
            return c


def driver():
    str = "abdabb"
    print ("Non Repeating Character is :",NonRepeating(str))


driver()