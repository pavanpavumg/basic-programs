def longsubstring(s):
    seen = set()
    left = 0
    max_string = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left+=1

        seen.add(s[right])

        max_string = max(max_string, right - left + 1)

    return max_string

sa = input()
print(longsubstring(sa))