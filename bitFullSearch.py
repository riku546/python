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


def bit_full_search(elements):
    all_subsets = []
    n = len(elements)

    for i in range(1 << n):
        subset = []

        for j in range(n):
            if i & (1 << j):
                print(elements[j])
                subset.append(elements[j])

        all_subsets.append(subset)

    return all_subsets


if __name__ == "__main__":
    # 使用例
    elements = [1, 2, 3]
    subsets = bit_full_search(elements)
    for subset in subsets:
        print(subset)
