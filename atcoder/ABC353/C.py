def sigma(N, A):
    total = 0
    for i in range(N):
        for j in range(i + 1, N):
            total += (A[i] + A[j]) % (10**8)

    return total


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    print(sigma(N, A))
