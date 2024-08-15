# def second_best(nums):
#     max_num = 0

#     for i in range(len(nums)):
#         if max_num < nums[i]:
#             max_num = nums[i]

#     second_num = 0
#     temp_index = 0
#     for j in range(len(nums)):
#         if max_num == nums[j]:
#             continue
#         elif second_num < nums[j]:
#             second_num = nums[j]
#             temp_index = j

#     return temp_index + 1


# # nums = [8, 2, 5, 1]
# nums = [1, 2, 3, 4, 5, 10, 9 ,11]
# print(second_best(nums))
