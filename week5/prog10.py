def factor():
    fact_1 = 1
    fact_all = 0
    n = int(input())
    for i in range(1, n + 1):
        fact_1 *= i
        fact_all += fact_1
    print(fact_all)


factor()
