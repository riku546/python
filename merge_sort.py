def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    center = len(nums) // 2
    left = nums[:center]
    right = nums[center:]

    merge_sort(left)
    merge_sort(right)
    
    


nums = [5, 4, 1, 8, 7, 3, 2, 9]
merge_sort(nums)
