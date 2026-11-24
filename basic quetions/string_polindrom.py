def polindrom(s):
    string = list(s)
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return "Not a polindrom"

        left+=1
        right-=1
    return "Polindrom"

s = input("enter a string")
print(polindrom(s))
