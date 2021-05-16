def pattern_of_triple_step(N: int):
    if N < 0:
        return 0
    elif N == 0:
        return 1
    else:
        return (
            pattern_of_triple_step(N - 1)
            + pattern_of_triple_step(N - 2)
            + pattern_of_triple_step(N - 3)
        )


if __name__ == "__main__":
    print(pattern_of_triple_step(1))
