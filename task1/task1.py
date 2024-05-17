def main(n: int, m: int) -> None:
    k = 1
    while True:
        print(k, end='')
        k = 1 + (k + m - 2) % n
        if k == 1:
            break
    print()


if __name__ == '__main__':
    print('Введите аргументы: n m (пример: 5 4)')
    n_val, m_val = map(int, input().split())
    main(
        n=n_val,
        m=m_val
    )
