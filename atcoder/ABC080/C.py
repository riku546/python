def bit_full_search(N, F, P):
    benefits = []
    for i in range(1, 1 << 10):
        temp = []
        benefit = 0
        for j in range(10):
            if i & (1 << j):
                temp.append(j)

        for n in range(N):
            count = len([t for t in temp if F[n][t] == 1])
            benefit += P[n][count]

        benefits.append(benefit)

    return max(benefits)


N = int(input())
Fs = []
Ps = []
F = [list(map(int, input().split())) for n in range(N)]
P = [list(map(int, input().split())) for n in range(N)]


print(bit_full_search(N, F, P))
