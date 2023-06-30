#!/usr/bin/python3
"""technical interview preparation
so much work done here love this"""

def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): List of unsorted integers.

    Returns:
        int or None: The peak element in the list or None if the list is empty.

    Complexity:
        The time complexity of this algorithm is O(log(n)), where n is the number of elements in the list.
        The space complexity is O(1).

    Note:
        There may be more than one peak in the list.
    """
    # Check if the list is empty
    if not list_of_integers:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        # Compare the middle element with its adjacent elements
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
