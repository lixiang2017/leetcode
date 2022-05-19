
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


def test_quick_sort():
    arr = [1, 5, 3, 2, 4, 1, 5, 3, 2, 4]
    print(quick_sort(arr))


def quick_sort_in_place(arr, left, right):
    if left >= right:
        return
    pivot = arr[left]
    i = left + 1
    j = right
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[j] = arr[j], arr[left]
    quick_sort_in_place(arr, left, j - 1)
    quick_sort_in_place(arr, j + 1, right)

def test_quick_sort_in_place():
    arr = [1, 5, 3, 2, 4, 1, 5, 3, 2, 4]
    quick_sort_in_place(arr, 0, len(arr) - 1)
    print(arr)


if __name__ == '__main__':
    test_quick_sort()
    test_quick_sort_in_place()