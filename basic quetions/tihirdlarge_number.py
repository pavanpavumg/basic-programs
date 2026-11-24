def thirdlarge_number(nums):
    large = 0
    second_large = 0
    third_large = 0

    for num in nums:
        if num > large:
            second_large = large
            large = num
        elif num > second_large:
            third_large = second_large
            second_large = num

        elif num > third_large:
            third_large = num

    return third_large

t = list(map(int, input().split()))
print(thirdlarge_number(t))