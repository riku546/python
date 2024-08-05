
def linear_search(numbers:list  , value:int) ->int:
  for i in range(len(numbers)):
    if numbers[i] == value:
      return i
    
  return -1


def binary_search(numbers:list , value:int) -> int:
  left , right = 0 , len(numbers) -1
  while left <= right:
    mid = (left + right ) //  2
    if numbers[mid] == value:
      return mid
    elif numbers[mid] < value:
      left = mid + 1
    else:
      right = mid - 1

  return -1

if __name__ == "__main__":
  nums = [0 , 1 , 5 , 7 , 9 , 11 , 15 , 20 , 24]
  print(binary_search(nums , 1))