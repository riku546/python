def formula(list_S, S):
    many_formula = []
    len_s = len(S)
    for i in range(1 << (len_s - 1)):
        temp = ["0" for i in range(len(S) - 1)]
        for j in range(len_s - 1):
            if i & (1 << j):
                temp[j] = "+"

        many_formula.append(temp)

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
