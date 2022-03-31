# function to check if two strings are
# anagram or not
def check(string1, string2):
    """
    :param string1: string of first word
    :param string2: string of second word
    :return: result of checking whether the given two strings are anagram or not using inbuilt sorted function
    """
    # the sorted strings are checked
    if sorted(string1) == sorted(string2):
        return "The strings are anagrams."
    else:
        return "The strings aren't anagrams."


if __name__ == "__main__":
    str1 = "listen"
    str2 = "silent"
    print(check(str1, str2))
