def reverse_string(s: str) -> str:
    letter = list(s)
    left = 0
    right = len(letter) - 1

    while left < right:
        letter[left], letter[right] = letter[right], letter[left]
        left+=1
        right-=1


    return "".join(letter)

st = input("enter string name:")

print(reverse_string(st))