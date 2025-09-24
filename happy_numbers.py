# Happy number function
def is_happy_num(n):
    seen = set()

    while n != 1:
        if n in seen:
            return False
        seen.add(n)

        str_n = str(n)
        str_arr = list(str_n)

        num_arr = [int(i) for i in str_arr]

        sqr_num_arr = [n**2 for n in num_arr]

        n = sum(sqr_num_arr)
    return True


# Get user input
while True:
    try:
        n = int(input("Enter a number (0 to exit): "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        continue

    if n == 0:
        break
    elif n < 0:
        print("Please enter a positive integer.")
        continue
    else:
        break

# Run happy number function
print(f"Is {n} a happy number?")
print("Yes!" if is_happy_num(n) else "No.")
