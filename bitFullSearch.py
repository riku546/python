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


# def multiple_table(N):
#     for i in range(1, 10):
#         for j in range(1, 10):
#             if (i * j) == N:
#                 return "Yes"

#     return "No"


# def bit_full_search(N, M, s, p):
#     result = 0
#     for i in range(1 << N):
#         is_all_on = True
#         for k in range(M):
#             count = 0

#             for j in range(s[k][0]):
#                 if i & (1 << (s[k][j + 1] - 1)):
#                     count += 1

#             if count % 2 != p[k]:
#                 is_all_on = False
#                 break

#         if is_all_on:
#             result += 1

#     return result


if __name__ == "__main__":
    pass
