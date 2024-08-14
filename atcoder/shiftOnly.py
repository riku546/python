import array
def shift_only(nums , length:int)->int:
  count = 0
  while True:
    for i in range(length):
      if nums[i] % 2 != 0: return count
      nums[i] //= 2
    count+=1 
  
nums = [3 , 12 , 24]
print(shift_only(nums , 3))