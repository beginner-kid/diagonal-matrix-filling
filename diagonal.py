def create():
    k = int(0)
    m = int(input("Enter number of rows :"))
    n = int(input("Enter number of columns :"))
    matrix = [[0 for i in range(n)] for j in range(m)]
    diagonals = m + n
    for l in range(diagonals):
        init_column = max(0, l - m)
        path = min(l, (n - init_column), m)

        for j in range(path):
            k = k + 1
            matrix[min(m, l) - j - 1][init_column + j] = k

    print("the obtained matrix is:")

    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end="\t")
        print("\n")


create()
