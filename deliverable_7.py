import pandas as pd #import pandas so that we can use dataframe

# asks the user to input any integer with a value greater than 0
n = int(input("Enter an integer value greater than 0: "))

# conditional statement checks user entry to ensure its greater than zero
if n > 0:
    # create lists for even, odd, and Fibonacci numbers
    even_numbers = list(range(0, 2*n, 2))
    odd_numbers = list(range(1, 2*n, 2))
    fibonacci_numbers = [0, 1]
    for i in range(2, n):
        fibonacci_numbers.append(fibonacci_numbers[i-1] + fibonacci_numbers[i-2])

    # create a data frame to display the results
    data = {
        "Even": even_numbers,
        "Odd": odd_numbers,
        "Fibonacci": fibonacci_numbers,
    }
    df = pd.DataFrame(data)
    print(df)

else:
    print("Please enter an integer value greater than 0.")

# pause at the end to allow the user to read output
input("Press Enter to exit...")
