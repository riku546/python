def bit_full_search(num):
    nums = [1 , "" , 2, "" , 5]
    len_num = len(str(num))
    for i in range(1 << (len_num - 1)):
        for j in range(len_num):
          if i & (1 << j):
            print(nums[j])


if __name__ == "__main__":
    bit_full_search(125)
