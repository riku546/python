def can_make_sum(index, current_sum, N, S, A):

    # 基底条件：目標の合計に達した場合
    if current_sum == S:
        return True

    # 基底条件：すべてのカードを確認したか、合計が目標を超えた場合
    if index == N or current_sum > S:
        return False

    # 現在のカードを選ぶ場合
    if can_make_sum(index + 1, current_sum + A[index], N, S, A):
        return True

    # 現在のカードを選ばない場合
    return can_make_sum(index + 1, current_sum, N, S, A)


if __name__ == "__main__":

    nums = [3, 1, 4, 5]
    N = 4
    S = 11

    print(can_make_sum(0, 0, N, S, nums))
