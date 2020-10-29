"""
Merge sort is a sorting algorithm, based on the divide and conquer strategy.
The array is divided into two halves and each of these halves are sorted recursively, and finally the sorted halves are merged back.
The run-time of merge sort is not affected by the nature of the input array.

Input: Unsorted array
Output: Sorted array

Time complexity: O(nlogn)
"""

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    left = []
    for i in range(n1):
        left.append(arr[l+i])
    
    right = []
    for i in range(n2):
        right.append(arr[m+i+1])

    i , j = 0 , 0
    k = l

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = (l + r) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

if __name__ == '__main__':
    arr = [int(x) for x in input('Enter the unsorted array: ').split()]
    n = len(arr)
    mergeSort(arr, 0, n-1)
    print('The array after sorting is:')
    print(arr)