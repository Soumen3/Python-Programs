def mergeSortAndCount(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        mid = len(arr) // 2
        left, left_inv = mergeSortAndCount(arr[:mid])
        right, right_inv = mergeSortAndCount(arr[mid:])
        merged, split_inv = mergeAndCount(left, right)
        return merged, left_inv + right_inv + split_inv
    
def mergeAndCount(left, right):
    merged = []
    split_inv = 0
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            split_inv += len(left) - i
    merged += left[i:]
    merged += right[j:]
    return merged, split_inv

print(mergeSortAndCount([8, 4, 2, 1]))