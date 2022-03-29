def find_word(L, target):
    start = 0
    end = len(L) - 1
    while start <= end:
        middle = (start + end) // 2
        midpoint = L[middle]
        if midpoint > target:
            end = middle - 1
        elif midpoint < target:
            start = middle + 1
        else:
            end = middle - 1
            return "word is present"
    return "word is not present"


if __name__ == "__main__" :
    L = ["Java", "C", "Python", "Html", "Css", "dotnet"]
    L = sorted(L)
    print(find_word(L, "Python"))
    print(find_word(L, "React"))
