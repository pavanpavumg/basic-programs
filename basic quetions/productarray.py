def product_except_self(nums):

    n = len(nums)

    left = [1] * n
    right = [1] * n
    ans = [1] * n

    # Calculate left products
    for i in range(1, n):
        left[i] = left[i-1] * nums[i-1]

    # Calculate right products
    for i in range(n-2, -1, -1):
        right[i] = right[i+1] * nums[i+1]

    # Multiply left and right products
    for i in range(n):
        ans[i] = left[i] * right[i]

    return ans


nums = list(map(int, input("Enter array elements: ").split()))

result = product_except_self(nums)

print("Output:", result)