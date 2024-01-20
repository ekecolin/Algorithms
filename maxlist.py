def maxlist(list_of_numbers):
    # base case
    if len(list_of_numbers) == 1:
        return list_of_numbers[0]

    #recursive case
    #otherwise
    head = list_of_numbers[0]
    maxtail = maxlist(list_of_numbers[1:])
    #return the bigger of the 2 head, maxtail
    return head if head > maxtail \
        else maxtail

def main():
    x = maxlist([3,1,5,4])
    print(x)

if __name__ == '__main__':
    main()