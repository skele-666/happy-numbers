# A happy number is defined by the following process. Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers. Display an example of your output here. Find first 8 happy numbers.

# Happy number function
def is_happy_num(n):
    while n != 1:
        str_n = str(n)
        str_arr = list(str_n)
        
        num_arr = [int(n) for n in str_arr]
        print(num_arr)

        sqr_num_arr = [n ** 2 for n in num_arr]
        print(sqr_num_arr)
        
        n = sum(sqr_num_arr)
        
        print(n)


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

print(n)
is_happy_num(n)
