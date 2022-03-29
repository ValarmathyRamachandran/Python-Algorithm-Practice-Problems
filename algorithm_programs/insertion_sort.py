# This function takes unsorted array as an input
# and returns sorted array.
def insertion_sort(arr):
    # loop over all the elements in the list
    for i in range(1, len(arr)):

        val = arr[i]

        # move elements of list [0..i-1], that are
        # greater than val, to one position ahead
        # of the current position
        j = i - 1
        while j >= 0 and val < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = val

    return arr


if __name__ == "__main__":
    # given string
    sample_string = "python"
    arr = [i for i in sample_string]
    sorted_arr = insertion_sort(arr)
    print(f"Original String: {sample_string}")
    print(f"Sorted String: {''.join(sorted_arr)}")
