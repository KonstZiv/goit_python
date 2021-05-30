def fibonacci(n):
    if n <= 1:
        return 0 or n
    return fibonacci(n-1) + fibonacci(n-2)


def main():
    n = None
    while n is None:
        try:
            n = int(input("введите целое положительное число: "))
            if n < 0:
                print(
                    f"Вы ввели {n}. Введенное число должнот быть положительным. Попробуйте еще раз.")

        except ValueError:
            print("вводимые символы должны быть целым числом")

    print(fibonacci(n))


if __name__ == "__main__":
    import sys
    for arg in sys.argv:
        print(arg)
    main()
