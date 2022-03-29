# Creating a bubble sort function
def bubble_sort(list):
    # Outer loop for traverse the entire list
    for i in range(0, len(list) - 1):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
    return list


if __name__ == "__main__":
    list1 = [5, 3, 8, 6, 7, 2]
    print("The unsorted list is: ", list1)
    # Calling the bubble sort function
    print("The sorted list is: ", bubble_sort(list1))