import copy


def formula(list_S, S):
    many_formula = []
    len_s = len(S)
    for i in range(1 << (len_s - 1)):

        copy_list_S = copy.copy(list_S)
        temp = ["0" for i in range(len_s - 1)]

        for j in range(len_s - 1):
            if i & (1 << j):
                temp[j] = "1"

        r = 0

        for k in range(1, len(list_S), 2):
            if temp[r] == "1":
                copy_list_S[k] = "+"
            r += 1

        many_formula.append(copy_list_S)

    return many_formula


def between_space(S):
    result = []

    for i, s in enumerate(S):
        result.append(s)

        if i < len(S) - 1:
            result.append("")

    return result


if __name__ == "__main__":
    S = input()
    list_S = between_space(S)
    print(formula(list_S, S))
