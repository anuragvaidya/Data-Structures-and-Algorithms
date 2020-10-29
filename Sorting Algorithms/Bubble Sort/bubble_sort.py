"""
Bubble sort is a sorting algorithm that sorts the array by comparing adjacent elements of the array.
On each iteration, the next largest element 'bubbles' to the end of the array, thus it gets the name bubble sort.
Bubble sort runs fastest when the array is already sorted, and slowest when the array is sorted in reverse order.

Input: Unsorted array
Output: Sorted array

Time complexity: O(n^2)
"""

import numpy as np

def bubble_sort(arr):
    n = arr.shape[0]
    for i in range(n):
        swap = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if not swap:
            break

if __name__ == '__main__':
    arr = np.array([int(x) for x in input('Enter the unsorted array: ').split()])
    bubble_sort(arr)
    print('The array after sorting is:')
    print(arr)