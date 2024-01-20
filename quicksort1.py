def quicksort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        # Defining our pivot
        # pop() removes the last element and also returns it
        pivot = sequence.pop()

    greater, lower=[],[]

    # Comparing each element to pivot point
    for item in sequence:
        if item > pivot:
            greater.append(item)
        else:
            lower.append(item)

    # Concatenating the lists together
    return quicksort(lower)+[pivot]+quicksort(greater)

print(quicksort([6,9,7,4,2,6,0,9,8,7,6,5,7]))