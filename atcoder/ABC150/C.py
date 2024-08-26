import itertools


def count_order(N, P, Q):
    N_array = [n for n in range(1, N + 1)]
    permutations_N = itertools.permutations(N_array)
    result_p = 0
    result_q = 0
    for i, permutation in enumerate(permutations_N):

        if permutation == P:
            result_p = i + 1

        if permutation == Q:
            result_q = i + 1

    return abs(result_q - result_p)


N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

print(count_order(N, P, Q))
