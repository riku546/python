def bit_full_search(N, M, X, C):
    all_combination = [i for i in range(N)]

    total_list = []
    for i in range(1 << N):
        temp_total = 0
        combination_temp = []
        for j in range(N):
            if i & (1 << j):
                combination_temp.append(j)

        if calc_colum_total(N, M, combination_temp, X, C) == False:
            continue

        for a in combination_temp:
            temp_total += C[a][0]

        total_list.append(temp_total)
    if len(total_list) == 0:
        return -1

    return min(total_list)


def calc_colum_total(N, M, combination_temp, X, C):
    for j in range(1, M + 1):
        total = 0
        for i in combination_temp:
            total += C[i][j]
        if total < X:
            return False


if __name__ == "__main__":
    N, M, X = list(map(int, input().split()))
    C = []
    for i in range(N):
        temp = list(map(int, input().split()))
        C.append(temp)

    print(bit_full_search(N, M, X, C))
