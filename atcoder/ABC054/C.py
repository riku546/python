import itertools


def one_stroke(N, M, ab):
    N_array = [n for n in range(1, N + 1)]
    permutation_N = itertools.permutations(N_array)
    custome_permutation_N = [
        permutation for permutation in permutation_N if permutation[0] == 1
    ]

    result = 0

    can_path = [[ab[m][1], ab[m][0]] for m in range(M)] + ab

    for permutation in custome_permutation_N:
        is_can_path = True
        for j in range(N - 1):
            if not [permutation[j], permutation[j + 1]] in can_path:
                is_can_path = False
                break

        if is_can_path:
            result += 1

    return result


N, M = list(map(int, input().split()))
ab = [list(map(int, input().split())) for m in range(M)]

print(one_stroke(N, M, ab))
