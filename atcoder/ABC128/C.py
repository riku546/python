def bit_search(N, M, K, P):
    result = []
    for i in range(1 << M):
        temp = []
        for j in range(M):
            if i & (1 << j):
                temp.append("ok")
            else:
                temp.append("off")

        # result.append(temp)

    return result


def count_valid_combinations(n, m, switches, p):
    valid_count = 0

    # 全てのスイッチの状態の組み合わせをビット全探索
    for i in range(2**n):
        is_valid = True

        # 全ての電球に対して点灯条件をチェック
        for j in range(m):
            on_count = 0
            for switch in switches[j]:
                if i & (1 << (switch - 1)):
                    on_count += 1

            if on_count % 2 != p[j]:
                is_valid = False
                break

        if is_valid:
            valid_count += 1

    return valid_count


# def example(nums):
#     result = []
#     n = len(nums)
#     for i in range(1 << n):
#         temp = []
#         for j in range(n):
#             if i & (1 << j):
#                 print(bin(i)[2:], bin(1 << j)[2:] , nums[j])
#                 temp.append(nums[j])

#         result.append(temp)
#     return result


def bit_full_search(N, S, A):
    for i in range(1 << N):
        total = 0
        for j in range(N):
            if i & (1 << j):
                total += A[j]

        if total == S:
            return "Yes"

    return "No"


if __name__ == "__main__":
    N, S = map(int, input().split())
    A = list(map(int, input().split()))
    print(bit_full_search(N, S, A))
