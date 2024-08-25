import itertools


def travel(N, K, T, N_array):
    permutations_result = itertools.permutations(N_array)
    result = 0
    
    for i, permutation in enumerate(permutations_result):
        total_time = 0
        
        total_time += T[0][permutation[0]]

        for j in range(N - 1):
            if j >= N - 2:
                total_time += T[permutation[j]][0]
            elif j < N - 1:
                total_time += T[permutation[j]][permutation[j + 1]]

        if total_time == K:
            result += 1

    return result


N, K = list(map(int, input().split()))
T = [list(map(int, input().split())) for n in range(N)]
N_array = [i for i in range(1, N )]
print(travel(N, K, T, N_array))
