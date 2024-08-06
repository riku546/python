def insertion_sort(numbers):
  len_number = len(numbers)
  for i in range(1 , len_number):
    temp = numbers[i]
    j = i - 1

    while j >=0 and numbers[j] > temp:
      numbers[j + 1] = numbers[j]
      j -= 1

    numbers[j + 1] = temp

  return numbers

if __name__ == "__main__":
  import random
  nums = [random.randint(1 , 35) for i in range(10)]
  print(insertion_sort(nums))