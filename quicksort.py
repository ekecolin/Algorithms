from random import randint

# Create randomized, unsorted arrays for testing
def create_array(size=10, max=50):
    return[randint(0,max) for n in range(size)]

# Applies quicksort to input array, returns sorted array
def quicksort(a):
    # check if len of array is LT or equal to 1, if so we just return a, because we know that any array of len 0 or 1 is sorted
    if len(a) <= 1:
        return a
    # Created 3 empty lists
    smaller, equal, larger=[],[],[]
    # Use randint func to select a random pivot in the input array using a randomised
    # pivot we can hope to avoid hitting the worst case time complexity by
    # avoiding selecting our pivot on the same location on every recursive call
    pivot=a[randint(0,len(a)-1)]

    # For loop
    for x in a:
        # If current element is smaller than the pivot it goes into the smaller list
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)

    # Returning the concatenation of the return value of quicksort calling on the smaller elements
    # all elements equal to the pivot and all elements larger than the pivot
    return quicksort(smaller)+quicksort(equal)+quicksort(larger)

# Ensuring quicksort algorithm is working properly
a = create_array()
print('Unsorted:', a)
s = quicksort(a)
print('Sorted', s)