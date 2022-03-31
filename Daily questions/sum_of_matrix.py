# Program to add two matrices using list comprehension
def sum_of_matrix():
    X = [[12, 7, 3],
         [4, 5, 6],
         [7, 8, 9]]

    Y = [[5, 8, 1],
         [6, 7, 3],
         [4, 5, 9]]

    result = [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

    for r in result:
        print(r)


if __name__ == "__main__":
    sum_of_matrix()
