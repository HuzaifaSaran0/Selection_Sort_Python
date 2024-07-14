# Selection Sort in Python

## Table of Contents

- [Introduction](#introduction)
- [Algorithm Explanation](#algorithm-explanation)
- [Complexity Analysis](#complexity-analysis)
- [Python Implementation](#python-implementation)
- [How to Run](#how-to-run)
- [Example](#example)
- [Usage](#usage)
- [References](#references)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Selection Sort is a simple comparison-based sorting algorithm. It divides the input list into two parts: the sublist of items already sorted and the sublist of items remaining to be sorted. The algorithm repeatedly selects the smallest (or largest, depending on the order) element from the unsorted sublist, swapping it with the leftmost unsorted element, and moving the sublist boundaries one element to the right.

## Algorithm Explanation

1. **Initialize:** Start with the first element of the list.
2. **Find Minimum:** Find the smallest element in the unsorted part of the list.
3. **Swap:** Swap this smallest element with the first element of the unsorted part.
4. **Repeat:** Move the boundary of the sorted and unsorted parts one element to the right and repeat until the entire list is sorted.

### Pseudocode
```python
for i = 0 to n-1
min_index = i
for j = i+1 to n
if array[j] < array[min_index]
min_index = j
swap array[i] with array[min_index]
```


## Complexity Analysis

- **Time Complexity:**
  - Best case: O(n²)
  - Average case: O(n²)
  - Worst case: O(n²)
- **Space Complexity:** O(1) (in-place sorting)
- **Stability:** Not stable

## Python Implementation

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr



