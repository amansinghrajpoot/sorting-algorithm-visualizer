import pygame
from abc import ABCMeta, abstractmethod


class Algorithm(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name  # Get name of the variable

    @abstractmethod
    def algorithm(self, data: list, vis):
        pass


# Add algorithms here

############################ Bubble sort ###################################


class BubbleSort(Algorithm):
    def __init__(self):
        super().__init__("BubbleSort")

    def algorithm(self, data: list, vis):
        for i in range(len(data)):
            for j in range(len(data) - 1 - i):
                if data[j] > data[j + 1]:  # last argument is milliseconds to wait because swapping can be fast
                    # and user will not see anything hence wait required
                    vis.update_display(data, j, j + 1, 0)  # Highlights which data is going to be swapped
                    data[j], data[j + 1] = data[j + 1], data[j]  # Swapping the data
                    vis.swap_display(data, j, j + 1, 0)  # Highlights the data which has been swapped.


############################ Selection sort ###################################


class SelectionSort(Algorithm):
    def __init__(self):
        super().__init__("SelectionSort")

    def algorithm(self, array: list, vis):
        for i in range(len(array)):
            min_idx = i
            for j in range(i + 1, len(array)):
                if array[j] < array[min_idx]:
                    min_idx = j
            vis.update_display(array, i, min_idx, 6)
            array[i], array[min_idx] = array[min_idx], array[i]
            vis.swap_display(array, i, min_idx, 6)


############################ Merge sort ###################################


class MergeSort(Algorithm):
    def __init__(self):
        super().__init__("MergeSort")

    def algorithm(self, arr: list, vis):
        self.mergeSort(arr, 0, len(arr) - 1, vis)

    def mergeSort(self, arr: list, l, r, vis):
        if l < r:
            # Same as (l+r)//2, but avoids overflow for
            # large l and h
            m = l + (r - l) // 2

            # Sort first and second halves
            self.mergeSort(arr, l, m, vis)
            self.mergeSort(arr, m + 1, r, vis)
            self.merge(arr, l, m, r, vis)

    def merge(self, arr: list, l, m, r, vis):
        n1 = m - l + 1
        n2 = r - m

        # create temp arrays
        L = [0] * n1
        R = [0] * n2

        # Copy data to temp arrays L[] and R[]
        for i in range(0, n1):
            L[i] = arr[l + i]

        for j in range(0, n2):
            R[j] = arr[m + 1 + j]

        # Merge the temp arrays back into arr[l..r]
        i = 0  # Initial index of first subarray
        j = 0  # Initial index of second subarray
        k = l  # Initial index of merged subarray

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                vis.update_display(arr, k, k, 4)
                arr[k] = L[i]
                vis.swap_display(arr, k, k, 4)
                i += 1
            else:
                vis.update_display(arr, k, k, 4)
                arr[k] = R[j]
                vis.swap_display(arr, k, k, 4)
                j += 1
            k += 1

        # Copy the remaining elements of L[], if there
        # are any
        while i < n1:
            vis.update_display(arr, k, k, 4)
            arr[k] = L[i]
            vis.swap_display(arr, k, i, 4)
            i += 1
            k += 1

        # Copy the remaining elements of R[], if there
        # are any
        while j < n2:
            vis.update_display(arr, k, k, 4)
            arr[k] = R[j]
            vis.swap_display(arr, k, k, 4)
            j += 1
            k += 1

    # l is for left index and r is right index of the
    # sub-array of arr to be sorted


############################ Quick sort ###################################


class QuickSort(Algorithm):
    def __init__(self):
        super().__init__("QuickSort")

    def algorithm(self, arr: list, vis):
        self.quicksort(0, len(arr) - 1, arr, vis)

    def partition(self, l, r, nums, vis):
        # Last element will be the pivot and the first element the pointer
        pivot, ptr = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                # Swapping values smaller than the pivot to the front
                vis.update_display(nums, i, ptr, 4)
                nums[i], nums[ptr] = nums[ptr], nums[i]
                vis.swap_display(nums, i, ptr, 4)
                ptr += 1
        # Finally swapping the last element with the pointer indexed number
        vis.update_display(nums, ptr, r, 4)
        nums[ptr], nums[r] = nums[r], nums[ptr]
        vis.swap_display(nums, ptr, r, 4)
        return ptr

    def quicksort(self, l, r, nums, vis):
        if len(nums) == 1:  # Terminating Condition for recursion. VERY IMPORTANT!
            return nums
        if l < r:
            pi = self.partition(l, r, nums, vis)
            self.quicksort(l, pi - 1, nums, vis)  # Recursively sorting the left values
            self.quicksort(pi + 1, r, nums, vis)  # Recursively sorting the right values
        return nums
