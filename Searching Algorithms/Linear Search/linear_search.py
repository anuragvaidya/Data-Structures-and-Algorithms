"""
Linear search is a searching algorithm that finds an element in an array.
As the name suggests, the algorithm sequentially checks each element of the array until either a match is found, or the entire array has been searched.

Input: Array of integers, Search element
Output: If search element exists in array, first index of search element, else -1

Time complexity: O(n)
"""

def linear_search(arr, key):
    for i, ele in enumerate(arr):
        if ele == key:
            return i
    return -1

if __name__ == '__main__':
    arr = [int(x) for x in input('Enter the array: ').split()]
    key = int(input('Enter search element: '))
    print(linear_search(arr, key))