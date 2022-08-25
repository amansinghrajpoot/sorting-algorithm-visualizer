import visualizer
import algorithms

__author__ = "Aman Singh Rajpoot"
__version__ = "1.0"
__copyright__ = "None"


def main():
    vis = visualizer.visualize()
    bubble_sort = algorithms.BubbleSort()
    selection_sort = algorithms.SelectionSort()
    merge_sort = algorithms.MergeSort()
    quick_sort = algorithms.QuickSort();
    sorting_map = {"Quick Sort": quick_sort, "Merge Sort": merge_sort,
                   "Selection Sort": selection_sort, "Bubble Sort": bubble_sort}
    vis.run(sorting_map)


if __name__ == "__main__":
    main()
