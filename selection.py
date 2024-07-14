def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        temp = arr[i]
        arr[i] = arr[minimum]
        arr[minimum] = temp

    return arr
