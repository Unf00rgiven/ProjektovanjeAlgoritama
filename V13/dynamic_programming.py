def reqLCS(S, n, T, m):     # rekurzivni LCS
    if n == -1 or m == -1:
        return 0
    if S[n] == T[m]:
        return 1 + reqLCS(S, n-1, T, m-1)
    else:
        return max(reqLCS(S, n-1, T, m), reqLCS(S, n, T, m-1))


def LCS_lenght(X, Y):
    m = len(X) + 1  # zbog 0-te kolone i vrste
    n = len(Y) + 1
    table = [[0 for i in range(n)] for j in range(m)]       # brojevi u tebeli
    direction = [[0 for i in range(n)] for j in range(m)]   # stelice u tabeli
    for i in range(1, m):
        for j in range(1, n):
            if X[i - 1] == Y[j - 1]:
                table[i][j] = table[i-1][j-1] + 1
                direction[i][j] = "<^"
            elif table[i-1][j] >= table[i][j-1]:
                table[i][j] = table[i-1][j]
                direction[i][j] = "^"
            else:
                table[i][j] = table[i][j-1]
                direction[i][j] = "<"
    return table, direction

def print_LCS(direction, X, i, j):
    if i == 0 or j == 0:
        return
    if direction[i][j] == "<^":
        print_LCS(direction, X, i-1, j-1)
        print(X[i - 1])
    elif direction[i][j] == "^":
        print_LCS(direction, X, i-1, j)
    else:
        print_LCS(direction, X, i, j-1)

if __name__ == "__main__":
    X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
    Y = ['B', 'D', 'C', 'A', 'B', 'A']

    print("Requsrsive LCS results is:")
    print(reqLCS(X, len(X) - 1, Y, len(Y) - 1))
    print("")


    nums, arrows = LCS_lenght(X, Y)

    for line in arrows:
        print(line)

    print("")

    for line in nums:
        print(line)

    print("")

    print_LCS(arrows, X, len(X), len(Y))
