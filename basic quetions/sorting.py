def leniarsearch(nums, target):
    for num in nums:
        if num == target:
            return num
        return -1


l = list(map(int, input().split()))
t = int(input("target"))
print(leniarsearch(l, t))