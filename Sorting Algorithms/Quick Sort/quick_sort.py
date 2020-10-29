"""
Quick sort is a sorting algorithm, based on the divide and conquer strategy.
It picks an element as the pivot and partitions the array around the picked pivot.
Quick sort is slowest when the input array is already sorted.

Input: Unsorted array
Output: Sorted array

Time complexity: O(n^2), but on average O(nlogn)
"""

def partition(arr, l, r):
    pivot = arr[r]
    i = l-1

    for j in range(l, r):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i

def quicksort(arr, l, r):
    if l < r:
        part = partition(arr, l, r)
        quicksort(arr, l, part-1)
        quicksort(arr, part+1, r)

if __name__ == '__main__':
    arr = [int(x) for x in input('Enter the unsorted array: ').split()]
    n = len(arr)
    quicksort(arr, 0, n-1)
    print('The array after sorting is:')
    print(arr)