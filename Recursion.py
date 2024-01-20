
# Recursively sum up numbers in list_of_numbers
def sumup(list_of_numbers):
    # base case
    # Is list of numbers empty?
    if list_of_numbers == []: # <-- If we are asked to sum up an empty list the answer is 0
        return 0
    # otherwise restate the problem as a simpler version of itself
    # Taking out the first number in the list and leaving the rest, like in the example
    # sumup calls sumup: this is the definition of recursion
    # Crucially this call to sumup is simpler than the current one
    return list_of_numbers[0] + sumup(list_of_numbers[1:])


def main():
    x = sumup([5,3,1,4])
    print(x)

if __name__ == '__main__':
    main()