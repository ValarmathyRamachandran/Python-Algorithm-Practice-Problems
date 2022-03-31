# Function to find minimum required
# time to schedule all process
def min_time(D, n, M):
    # Stores max element from A[]
    max_ability = D[0]

    # Find the maximum element
    for i in range(1, n):
        max_ability = max(max_ability, D[i])

    # Stores frequency of each element
    tmp = [0 for i in range(max_ability + 1)]

    # Stores minimum time required
    # to schedule all process
    count = 0

    # Count frequencies of elements
    for i in range(n):
        tmp[D[i]] += 1

    # Find the minimum time
    i = max_ability

    while (i >= 0):
        if (tmp[i] != 0):
            if (tmp[i] * i < M):

                # Decrease the value
                # of M
                M -= (i * tmp[i])

                # Increment tmp[i/2]
                tmp[i // 2] += tmp[i]

                # Increment the count
                count += tmp[i]

                # Return count, if all
                # process are scheduled
                if M <= 0:
                    return count
            else:

                # Increment count
                if M % i != 0:
                    count += (M // i) + 1
                else:
                    count += (M // i)

                # Return the count
                return count
        i -= 1

    # If it is not possible to
    # schedule all process
    return -1


if __name__ == '__main__':
    arr = [3, 1, 7, 2, 4]
    D = 5
    M = 15

    print(min_time(arr, D, M))
