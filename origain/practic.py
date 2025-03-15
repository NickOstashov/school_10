def main():
    n = int(input("n: "))
    m = int(input("m: "))

    dp = list()

    dp_line = list()
    for i in range(n):
        dp_line.append(1)

    dp.append(dp_line)

    for _ in range(m - 1):
        dp_line = list()
        for i in range(n):
            if i == 0:
                dp_line.append(1)
            else:
                dp_line.append(0)
        dp.append(dp_line)

    for i in range(1, n):
        for  j in range(1, m):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]

    print(dp[n-1][m-1])


if __name__ == "__main__":
    main()