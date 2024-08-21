# def bit_full_search(elements):
#     n = len(elements)
#     all_subsets = []

#     # 2^n 通りの部分集合を生成
#     for i in range(1 << n):  # 1 << n は 2^n を意味する
#         subset = []

#         for j in range(n):
#             print(i, j)
#             # i の j ビット目が 1 ならば elements[j] を部分集合に含める
#             if i & (1 << j):
#                 subset.append(elements[j])
#         all_subsets.append(subset)

#     # return all_subsets


# def bit_full_search(elements):
#     all_subsets = []
#     n = len(elements)

#     for i in range(1 << n):
#         subset = []

#         for j in range(n):
#             if i & (1 << j):
#                 print(elements[j])
#                 subset.append(elements[j])

#         all_subsets.append(subset)

#     return all_subsets


def multiple_table(N):
    for i in range(1, 10):
        for j in range(1, 10):
            if (i * j) == N:
                return "Yes"

    return "No"


if __name__ == "__main__":
    N = int(input())
    print(multiple_table(N))
