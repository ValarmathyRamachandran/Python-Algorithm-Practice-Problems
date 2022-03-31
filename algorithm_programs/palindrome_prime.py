def palindrome_prime():
    min_range = 0
    max_range = 1000
    min_range += 1
    for i in range(min_range, max_range):
        y = True
        if str(i) == str(i)[::-1]:
            if i > 2:
                for a in range(2, i):
                    if i % a == 0:
                        y = False
                        break
                if y:
                    print(i)
    return i


if __name__ == "__main__":
    print(palindrome_prime())
