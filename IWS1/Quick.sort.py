def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
        arr = arr.copy()
    if low < high:
        pi = randomized_partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr

def randomized_partition(arr, low, high):
    rand_idx = random.randint(low, high)
    arr[rand_idx], arr[high] = arr[high], arr[rand_idx]
    return partition_lomuto(arr, low, high)
