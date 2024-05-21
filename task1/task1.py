import sys


def main(n: int, m: int) -> None:
    k = 1
    while True:
        print(k, end='')
        k = 1 + (k + m - 2) % n
        if k == 1:
            break
    print()


if __name__ == '__main__':
    main(
        n=int(sys.argv[1]),
        m=int(sys.argv[2])
    )
