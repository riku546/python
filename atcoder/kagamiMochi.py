
def liner_search(i , nums , temp):
  flag = False
  for j in range(len(temp)):
    if nums[i] == temp[j]: flag = True
  return flag

def binary_search(nums , n):
  sorted_nums = sorted(nums)
  left = 0
  right = len(sorted_nums) - 1
  
  while left <= right:
    mid = (left + right ) // 2
    if sorted_nums[mid] == n:
      return True
    if sorted_nums[mid] > n:
      right = mid - 1
    if sorted_nums[mid] < n:
      left = mid + 1
  return False
  



def kagami(nums):
  temp = [nums[0]]
  
  for i in range(1 ,len(nums)):
    print(temp , nums[i])
    if binary_search(temp , nums[i]) == False:
      temp.append(nums[i])

   
  return temp
    

    
  
d = [8 , 10 , 8 , 4 , 10 , 2 , 4]
print(kagami(d))