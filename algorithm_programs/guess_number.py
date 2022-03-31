def guess_number():
    """
    :return: guess number you have chosen in your mind from the range
    """
    arr = []
    num = 0

    max_range = int(input("Enter the maximum number: "))
    hint = max_range
    for i in range(max_range):
        arr.append(i)
    print("Take a number in your mind between 1 to range :)\nI am going to guess your number \n\n")

    while num <= hint:
        mid = (num + hint) // 2
        print("I think ", arr[mid], "is your number ?  If agree Press 'y' , If less than this Press 'L'  "
                                    "If greater Press 'G' ")
        ans = input("Enter the choice Y or L or G")
        if ans == 'Y' or ans == 'y':
            {
                print("\n\nYour number is : ", arr[mid])
            }
        elif ans == 'l' or ans == 'L':
            hint = mid - 1
        elif ans == 'g' or ans == 'G':
            num = mid + 1
    return


if __name__ =="__main__" :
    guess_number()
