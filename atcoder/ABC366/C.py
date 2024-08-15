def minimum_glutton(A, B, X, Y, N):
    sorted_A = []
    sorted_B = []
    temp_A = 0
    temp_B = 0
    count_A = 0
    count_B = 0
    
    sorted_A = selection_sort(A)
    sorted_B = selection_sort(B)
    for i in range(len(sorted_A)):
      temp_A += sorted_A[i]
      if temp_A > X:
        count_A = i + 1
        break
      
    for i in range(len(sorted_B)):
      temp_B += sorted_B[i]
      if temp_B > Y:
        count_B = i + 1
        break
      
    return min(count_B ,count_A)


def selection_sort(nums):
    for i in range(len(nums) - 1, -1, -1):
        temp = i
        for j in range(i - 1, -1, -1):
            if nums[temp] > nums[j]:
                temp = j
        nums[i], nums[temp] = nums[temp], nums[i]

    return nums




A = [2, 3, 5, 1]
B = [8, 8, 1, 4]

# A = [1 ,1 ,1 ,1 ,1]
# B = [2 ,2 ,2 ,2 ,2]

A=[1,2,3,4,5,6,7,8]
B= [8,7,6,5,4,3,2,1]
print(minimum_glutton(A, B, 30,30 , 6))
