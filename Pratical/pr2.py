def accepts_ending_with_ab(string):
    if string.endswith("ab"):
        return True
    else:
        return False

 
strings = ["ab", "cab", "aab", "abc", "helloab", "aba"]

for string in strings:
    if accepts_ending_with_ab(string):
        print(string, "-> Accepted")
    else:
        print(string, "-> Rejected")
