def solution(A):
    N = len(A)
    data = [0] * (N + 2)

    for x in A:
        if x <= 0 or x > N:
            return 0
        data[x] += 1

    for i in range(1, N + 1):
        if data[i] != 1:
            return 0
    return 1


def solution_better(A):
    data = [False] * len(A)

    for x in A:
        if x <= 0 or x > len(A):
            return 0
        if data[x - 1] == True:
            return 0
        data[x - 1] = True
    return 1
