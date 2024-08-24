# def merge_sort(nums):
#     if len(nums) <= 1:
#         return nums

#     center = len(nums) // 2
#     left = nums[:center]
#     right = nums[center:]

#     merge_sort(left)
#     merge_sort(right)

#     i = j = k = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             nums[k] = left[i]
#             i += 1
#         else:
#             nums[k] = right[j]
#             j += 1

#         k += 1

#     while i < len(left):
#         nums[k] = left[i]
#         i += 1
#         k += 1

#     while j < len(right):
#         nums[k] = right[j]
#         j += 1
#         k += 1

#     return nums


# def merge_sort(nums):
#     if len(nums) <= 1:
#         return nums

#     center = len(nums) // 2
#     left = nums[:center]
#     right = nums[center:]

#     merge_sort(left)
#     merge_sort(right)

#     i = j = k = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             nums[k] = left[i]
#             i += 1
#         else:
#             nums[k] = right[j]
#             j += 1

#         k += 1

#     while i < len(left):
#         print(k)
#         nums[k] = left[i]
#         i += 1
#         k += 1

#     while j < len(right):
#         print(k)
#         nums[k] = right[j]
#         j += 1
#         k += 1

#     return nums


# def merge_sort(nums):
#     if len(nums) <= 1:
#         return nums

#     center = len(nums) // 2
#     left = nums[:center]
#     right = nums[center:]

#     merge_sort(left)
#     merge_sort(right)

#     i = j = k = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             nums[k] = left[i]
#             i += 1
#         else:
#             nums[k] = right[j]
#             j += 1

#         k += 1

#     while i < len(left):
#         nums[k] = left[i]
#         i += 1
#         k += 1

#     while j < len(right):
#         nums[k] = right[j]
#         j += 1
#         k += 1

#     return nums


# def merge_sort(nums):
#     if len(nums) <= 1:
#         return nums

#     center = len(nums) // 2
#     left = nums[:center]
#     right = nums[center:]

#     merge_sort(left)
#     merge_sort(right)

#     i = j = k = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             nums[k] = left[i]
#             i += 1
#         else:
#             nums[k] = right[j]
#             j += 1

#         k += 1

#     while i < len(left):
#         nums[k] = left[i]
#         i += 1
#         k += 1

#     while j < len(right):
#         nums[k] = right[j]
#         j += 1
#         k += 1

#     return nums


# def merge_sort(nums):
#     if len(nums) <= 1:
#         return nums

#     center = len(nums) // 2
#     left = nums[:center]
#     right = nums[center:]

#     merge_sort(left)
#     merge_sort(right)

#     i = j = k = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             nums[k] = left[i]

#             i += 1
#             k += 1
#         else:
#             nums[k] = right[j]

#             j += 1
#             k += 1

#     while i < len(left):
#         nums[k] = left[i]
#         i += 1
#         k += 1

#     while j < len(right):
#         nums[k] = right[j]
#         j += 1
#         k += 1

#     return nums


if __name__ == "__main__":

    nums = [5, 4, 1, 8, 7, 3, 2, 9]
    print(merge_sort(nums))
