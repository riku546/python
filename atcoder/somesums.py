def somesums(N:int , A:int , B:int):
  total = 0
  for i in range(1 , N + 1):
    temp  = 0
    for j in str(i):
      temp += int(j)
    if temp <= B and temp >= A:
      total += i
  return total

print(somesums(20 , 2 , 5))