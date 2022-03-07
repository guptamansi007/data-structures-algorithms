def NonRepeating(str):


    count = {}

    for c in str:
        if c not in count:
            count[c] = 1
        else:
            count[c] = count[c] + 1

    if count[c] == 1:
        return c


def driver():
    str = "abababccd"
    print ("non repeating character is :",NonRepeating(str))


driver()