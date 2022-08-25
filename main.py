import visualizer
import algorithms

__author__ = "Aman Singh Rajpoot"
__version__ = "1.0"
__copyright__ = "None"


def main():
    vis = visualizer.visualize()
    bubble_sort = algorithms.BubbleSort()
    selection_sort = algorithms.SelectionSort()
    sorting_map = {"Selection Sort": selection_sort, "Bubble Sort": bubble_sort}
    vis.run(sorting_map)


if __name__ == "__main__":
    main()
