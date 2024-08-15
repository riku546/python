def coins (x , A  , B , C):
  count = 0
  for i in range(A + 1):
    for j in range(B + 1):
      for s in range(C + 1):
        result = (500 * i ) + (100 * j) + (50 * s)
        if result == x: count+=1
  return count

print(coins(100 , 2 , 2 ,2))