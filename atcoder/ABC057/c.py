def digits_example(N):
    temp = []

    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            temp.append(max((len(str(i)), len(str(N // i)))))

    if len(temp) == 0:
        return len(str(N))

    return min(temp)


if __name__ == "__main__":
    N = int(input())
    print(digits_example(N))
