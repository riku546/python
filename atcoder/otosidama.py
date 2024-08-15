# def otoshidama(nums , n ,y):
#   result = [-1 , -1 , -1]
#   temp = y 
#   total_calc_count = 0
#   for i in range(len(nums)):
#     print(i)
#     calc_count = 0
#     for j in range(n - total_calc_count):
#       print("j" )
#       temp -= nums[i]
      
#       if temp < 0 : break
      
#       calc_count+=1

#     total_calc_count += calc_count
#     result[i] = calc_count

#   return result

# print(otoshidama([10000 , 5000 , 1000] , 9 , 45000))


def otoshidama(nums , y , n):
  for i in range(n):
    for j in range(n - i):
      for x in range(n - i -j):
        if (10000 * i ) + (5000 * j) + (1000 * x) == y:
          return [i , j , x]
  return [-1 , -1 , -1]


nums = [10000 , 5000 , 1000]
print(otoshidama(nums , 45000 , 9))