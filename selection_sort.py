# from typing import List

# def selection_sort(numbers:List[int])->List[int]:
#   len_number = len(numbers)
#   for i in range(len_number):
#     min_index = i
#     for j in range(i + 1 , len_number):
#       if numbers[min_index] > numbers[j]:
#         min_index = j

#     numbers[i] , numbers[min_index]  = numbers[min_index] , numbers[i]

#   return numbers











def selection_sort(numbers):
  len_numbers = len(numbers)
  for i in range(len_numbers):
    min_index = i
    
    for j in range(i , len_numbers):
      if numbers[min_index] > numbers[j]:
        min_index = j

    numbers[i] , numbers[min_index] = numbers[min_index] , numbers[i]

  return numbers



if __name__ == "__main__":
  import random
  nums = [random.randint(0 , 10) for i in range(10)]
  print(selection_sort(nums))
