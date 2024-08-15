#引数  ["dream" , "dreamer" , "erase" , "eraser"]
#返り値 ['dreamer', 'erase', 'eraser', 'dream']
def change_order(string_list):
  first_num = string_list[0]
  for i in range(1 , len(string_list)):
    string_list[i - 1] = string_list[i]
  string_list[len(string_list) - 1] = first_num
  return string_list


def daydream(string_list , S):
  pass
  
  

string_list = ["dream" , "dreamer" , "erase" , "eraser"]
print(daydream(string_list  , "dreameraser"))