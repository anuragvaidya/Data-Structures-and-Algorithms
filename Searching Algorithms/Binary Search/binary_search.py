"""
Binary search is a searching algorithm that finds an element in a SORTED array.
On each iteration, the search element is compared with the middle element of the search array.
If the middle element matches with the search element, the index is returned.
If the search element is less than the middle element, we discard the second half of the search array and search in the first half.
If the search element is more than the middle element, we discard the first half of the search array and search in the second half.
Thus, on each iteration, we effectively reduce search region by half, hence the name binary search.
However, it is necessary that the elements of the array MUST be sorted.

Input: SORTED array of integers, Search element
Output: If search element exists in array, index of search element, else -1

Time complexity: O(log(n))
"""

def binary_search(arr, key):
    l = 0
    u = len(arr) - 1

    while l <= u:
        m = (l + u) // 2
        if arr[m] == key:
            return m
        elif key < arr[m]:
            u = m - 1
        else:
            l = m + 1
    return -1

if __name__ == '__main__':
    arr = [int(x) for x in input('Enter a sorted array: ').split()]
    key = int(input('Enter search element: '))
    print(binary_search(arr, key))