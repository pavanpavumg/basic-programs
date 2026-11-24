def maxProduct(nums: list[int]) -> int:
        max_num = nums[0]
        min_num = nums[0]
        ans = nums[0]

        for num in nums[1:]:
            if num < 0:
                max_num, min_num = min_num, max_num

            max_num = max(num, max_num * num)
            min_num = min(num, min_num * num)

            ans = max(ans, max_num)

        return ans

n = int(input("enter sub array size:"))
nums = list(map(int, input("enter array elements:").split()))
print(maxProduct(nums))
