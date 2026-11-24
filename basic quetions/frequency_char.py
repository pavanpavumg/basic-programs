def frequency_char(s):
    frq = {}
    count = 0

    for char in s:
        frq[char] = frq.get(char, 0) + 1
        count += 1

    return frq

f = input()
print(frequency_char(f))