def can_x(N, M, L, A, B, C):
    S = set()
    for i in range(N):
        for j in range(M):
            for t in range(L):
                S.add(A[i] + B[j] + C[t])

    return S


N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
L = int(input())
C = list(map(int, input().split()))
Q = int(input())
X = list(map(int, input().split()))


set = can_x(N, M, L, A, B, C)
for num in X:
    if num in set:
        print("Yes")
    else:
        print("No")
