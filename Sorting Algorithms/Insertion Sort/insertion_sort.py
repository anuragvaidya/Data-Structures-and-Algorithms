"""
Insertion sort is a sorting algorithm that sorts by inserting the next element into its appropriate position in the sorted subarray.
The first element of the array is assumed to be a sorted subarray.
Then on each iteration for the remaining elements, we find it's position in the sorted subarray before it and insert the element into that position.
Insertion sort runs fastest when the array is already sorted, and slowest when the array is sorted in reverse order.

Input: Unsorted array
Output: Sorted array

Time complexity: O(n^2)
"""

import numpy as np

def insertion_sort(arr):
    n = arr.shape[0]
    for i in range(1,n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


if __name__ == '__main__':
    arr = np.array([int(x) for x in input('Enter the unsorted array: ').split()])
    insertion_sort(arr)
    print('The array after sorting is:')
    print(arr)