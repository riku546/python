# def handle(nums, H, W):
#     result = []
#     for i in range(H):
#         result_child = []
#         for j in range(W):
#             total = calc_total_h_w(nums, H, W, i, j)
#             result_child.append(total)
#         result.append(result_child)
#     return result




# def calc_total_h_w(nums, H, W, current_H, current_W):
#     total = 0

#     for i in range(H):
#         total += nums[i][current_W]

#     for i in range(W):
#         total += nums[current_H][i]

#     # 上の2つのforで２回足してる分を引き算する
#     total -= nums[current_H][current_W]

#     return total


# nums = [
#     [31, 41, 59, 26, 53, 58, 97, 93, 23, 84],
#     [62, 64, 33, 83, 27, 95, 2, 88, 41, 97],
# ]

# print(handle(nums, 2, 10))