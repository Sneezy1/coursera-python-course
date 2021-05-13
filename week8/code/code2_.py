numbers = map(int, input().split())
print(
    *filter(
        lambda x: x > 0,
        map(
            int,
            input().split()
        )
    )
)
