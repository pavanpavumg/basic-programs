def second_largenumber(nums):

    maximum_number = 0
    second_number = 0
    maximum_number = nums[0]

    for num in nums:
        if num > maximum_number:
            second_number = maximum_number
            maximum_number = num
        elif num > second_number:
            second_number = num


    return second_number

s = list(map(int, input().split()))
print(second_largenumber(s))
         
