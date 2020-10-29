"""
Selection sort is a sorting algorithm that sorts the array by selecting the smallest element in the subarray.
On each iteration, the next smallest element of the subarray is selected and is put at the front of the subarray.
The run-time of selection sort is not affected by the nature of input array.

Input: Unsorted array
Output: Sorted array

Time complexity: O(n^2)
"""

import numpy as np

def selection_sort(arr):
    n = arr.shape[0]
    for i in range(n-1):
        small = arr[i]
        pos = i
        for j in range(i+1, n):
            if arr[j] < small:
                small = arr[j]
                pos = j
        arr[i], arr[pos] = arr[pos], arr[i]

if __name__ == '__main__':
    arr = np.array([int(x) for x in input('Enter the unsorted array: ').split()])
    selection_sort(arr)
    print('The array after sorting is:')
    print(arr)