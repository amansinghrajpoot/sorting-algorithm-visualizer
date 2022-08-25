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

############################ Quick sort ###################################
