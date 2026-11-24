def minWindow(s, t):

    if len(t) > len(s):
        return ""

    window = {}
    required = {}

    for char in t:
        required[char] = required.get(char, 0) + 1

    left = 0
    count = 0

    min_length = float("inf")
    start = 0

    for right in range(len(s)):

        char = s[right]

        window[char] = window.get(char, 0) + 1

        if char in required and window[char] <= required[char]:
            count += 1

        while count == len(t):

            if right - left + 1 < min_length:
                min_length = right - left + 1
                start = left

            left_char = s[left]

            window[left_char] -= 1

            if left_char in required and window[left_char] < required[left_char]:
                count -= 1

            left += 1

    if min_length == float("inf"):
        return ""

    return s[start:start + min_length]


s = input("Enter string: ")
t = input("Enter target string: ")

print("Minimum window:", minWindow(s, t))