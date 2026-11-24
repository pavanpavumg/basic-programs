# def polyndrom(num):

#     num_str = str(num)
#     left = 0
#     right = len(num_str) - 1

#     while left < right:
#         if num_str[left] != num_str[right]:
#             return "number is not palindrome"

        
#         left+=1
#         right-=1
#     return "number is palindrome"

# n = int(input("enter a number"))
# print(polyndrom(n))



num = int(input("enter a number"))
nums = list(str(num))
left = 0
mid = 0
right = len(nums) - 1
while mid <= right:
    if mid == 0:
        nums[mid], nums[left] = nums[left], nums[mid]
        left+=1
        mid+=1

    elif mid == 1:
        mid+=1

    else:
        nums[mid], nums[right] = nums[right], nums[mid]
        right-=1