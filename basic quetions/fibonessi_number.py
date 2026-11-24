def fibonacci(nums):
    first = 0
    second = 1

    for count in range(nums):
        print(first)

        current = first + second

        first = second
        second= current
        


n = int(input())
print(fibonacci(n))