def fibonacci_generator(n):
    # Initialize variables for the first two Fibonacci numbers
    a, b = 0, 1

    # Generate Fibonacci sequence up to the nth number
    for _ in range(n):
        yield a
        a, b = b, a + b


def main():
    print("Welcome to the Fibonacci Number Generator!")
    while True:
        try:
            n = int(input("Enter the number of Fibonacci numbers to generate (0 to exit): "))
            if n < 0:
                print("Please enter a non-negative integer.")
                continue
            elif n == 0:
                print("Exiting the program. Goodbye!")
                break
            else:
                # Generate Fibonacci numbers using the generator
                fib_gen = fibonacci_generator(n)
                fibonacci_numbers = list(fib_gen)

                # Print the generated Fibonacci numbers
                print("Generated Fibonacci numbers:", fibonacci_numbers)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
