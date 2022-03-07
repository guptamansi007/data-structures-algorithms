"""
Q : Given an array, find the most frequent elements in it. If there are multiple elements that appear a maximum number of times, print all of them.
Time complexity: 0(N)
Space complexity: O(N)
"""


def most_frequent_items(a):
    frequency_dict = {}
    max_frequency = 0
    max_frequency_items = []

    for item in a:
        if item not in frequency_dict:
            frequency_dict[item] = 1
        else:
            frequency_dict[item] += 1

        if frequency_dict[item] > max_frequency:
            max_frequency = frequency_dict[item]

    for item in frequency_dict:
        if frequency_dict[item] == max_frequency:
            max_frequency_items.append(item)

    return max_frequency_items;


def driver():
    a = [2, 2, 5, 5, 1, 5, 1, 5, 2, 1, 1]
    print("most frequent element is/are:", most_frequent_items(a))

driver()
