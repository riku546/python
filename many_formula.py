# import copy


# def formula(list_S, S):
#     total = 0
#     len_s = len(S)
#     for i in range(1 << (len_s - 1)):

#         copy_list_S = copy.copy(list_S)
#         temp = ["0" for i in range(len_s - 1)]

#         for j in range(len_s - 1):
#             if i & (1 << j):
#                 temp[j] = "1"

#         r = 0

#         for k in range(1, len(list_S), 2):
#             if temp[r] == "1":
#                 copy_list_S[k] = "+"
#             r += 1

#         temp_s = ""
#         for e in range(len(copy_list_S)):
#             temp_s += copy_list_S[e]

#         split_temp_s = temp_s.split("+")
#         for w in range(len(split_temp_s)):
#             total += int(split_temp_s[w])

#     return total


# def between_space(S):
#     result = []

#     for i, s in enumerate(S):
#         result.append(s)

#         if i < len(S) - 1:
#             result.append("")

#     return result


# if __name__ == "__main__":
#     S = input()
#     list_S = between_space(S)
#     print(formula(list_S, S))
