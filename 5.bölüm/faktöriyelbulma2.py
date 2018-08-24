while True:
    fact = input(
        "\nEnter the value that you want to find its factorial result (Enter 'E' if you wish to terminate the program): ")

    if fact == "e":
        print("\nThe program is terminated!")
        break
    else:
        fact = int(fact)

        if fact < 0:
            fact *= -1

        factorial = 1

        for i in range(1, fact + 1):
            factorial *= i

        print("\n{}! = {}".format(fact, factorial))