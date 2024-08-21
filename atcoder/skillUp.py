def bit_full_search(N):
  for i in range(2 ** N):
    for j in range(N):
      if i & (1 << j):
        pass
    
    
  
if __name__ == "__main__":
  N , M , X = list(map(int , input().split()))
  C = []
  for i in range(N):
    temp = list(map(int , input().split()))
    C.append(temp)

  
      