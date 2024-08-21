# def selectionSort(nums):
#   length_nums = len(nums)
#   for i in range(length_nums - 1 , -1 , -1):
#     temp = i
#     for j in range(i -1 , -1 , -1):
#       if nums[temp] > nums[j]:
#         temp = j
#     nums[i] , nums[temp] = nums[temp] , nums[i]

#   return nums

# # import random
# # nums = [random.randint(0, 100) for i in range(10)]
# # print(selectionSort(nums))

# a = [2 , 7 ,4]
# sorted_a = selectionSort(a)
# alice = 0
# bob = 0
# for i in range(len(a)):

#   if i % 2 == 0:
#     alice += sorted_a[i]
#   else:
#     bob += sorted_a[i]

# print(alice - bob)


def sort_example(N, A):
    result = []
    count = 0
    for i in range(N):
        if A[i] != i + 1:
            result.append([A[i], A[A[i] - 1]])
            A[A[i] - 1], A[i] = A[i], A[A[i] - 1]
            count += 1
    return result, count


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    result, count = sort_example(N, A)
    print(count)
    for i in range(count):
        print(result[i][1], result[i][0])
