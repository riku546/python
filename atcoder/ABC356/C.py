def test_keys(temp, C, K):
    for x in range(len(C)):

        count = 0

        for m in range(1, int(C[x][0]) + 1):

            if int(C[x][m]) in temp:
                count += 1

        if C[x][-1] == "o":
            if count < K:
                return False

        elif C[x][-1] == "x":
            if count >= K:
                return False

    return True


def keys(N, M, K, C):
    result = 0
    for i in range(2**N):
        temp = []

        for j in range(N):
            if i & (1 << j):
                temp.append(j + 1)

        if test_keys(temp, C, K):
            result += 1

    return result


if __name__ == "__main__":
    N, M, K = list(map(int, input().split()))
    C = [list(input().split()) for i in range(M)]

    print(keys(N, M, K, C))
