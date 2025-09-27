# Happy number function
def is_happy_num(n):
    seen = set()

    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        str_arr = list(str(n))
        num_arr = [int(i) for i in str_arr]
        sqr_num_arr = [n**2 for n in num_arr]
        n = sum(sqr_num_arr)
    return True


# Main program
def main():
    print(
        "Would you like to: (1) check an individual number, (2) see the first 8 happy numbers, or (0) exit?"
    )
    choice = ""
    while choice not in ["1", "2", "0"]:
        choice = input("Enter 1, 2 or 0: ")

    if choice == "1":
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

        if n != 0:
            # Run happy number function
            print(f"Is {n} a happy number?")
            print("Yes!" if is_happy_num(n) else "No.")
    elif choice == "2":
        happy_numbers = []
        num = 1
        while len(happy_numbers) < 8:
            if is_happy_num(num):
                happy_numbers.append(num)
            num += 1

        print("The first 8 happy numbers:")
        print(happy_numbers)
    else:
        print("Goodbye!")


if __name__ == "__main__":
    main()
