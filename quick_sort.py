def partition(nums, low, high):
    i = low - 1
    pivot = nums[high]
    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[j], nums[i] = nums[i], nums[j]

    nums[i + 1], nums[high] = nums[high] , nums[i + 1]

    return i + 1


def quick_sort(nums, low: int, high: int):
    if low < high:
        partition_index = partition(nums, low, high)
        quick_sort(nums, low, partition_index - 1)
        quick_sort(nums, partition_index + 1, high)
    return nums


def sort_processor(nums):
    sorted_nums = quick_sort(nums, 0, len(nums) - 1)
    return sorted_nums


if __name__ == "__main__":
    import random
    nums = [1, 8, 3, 9, 4, 5, 7]
    nums = [random.randint(0 , 1000) for i in range(100000)]
    print(sort_processor(nums))
