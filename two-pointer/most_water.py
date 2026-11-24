# nums = [1, 4, 6, 4, 9, 10, 60, 3]

def contaoner_most_water(nums):
    left = 0
    right = len(nums) - 1
    max_area = 0

    while left < right:
        current_area = min(nums[left], nums[right]) * (right - left)
        max_area = max(max_area, current_area)

        if left < nums[right]:
            left+=1
        else:

            right-=1

    return max_area

area = list(map(int, input().split()))
print(contaoner_most_water(area))
