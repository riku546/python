import itertools
import math


def calc(first, second):
    return (((first[1] - second[1]) ** 2) + ((first[0] - second[0]) ** 2)) ** 0.5


def average_length(N, xy):
    total = 0
    N_array = [i for i in range(N)]
    permutations_N = itertools.permutations(N_array)
    for permutation in permutations_N:
        temp = 0
        for i in range(N - 1):
            first, second = xy[permutation[i]], xy[permutation[i + 1]]
            temp += calc(first, second)

        total += temp

    return total / math.factorial(N)


N = int(input())
xy = [list(map(int, input().split())) for n in range(N)]
print(average_length(N, xy))
