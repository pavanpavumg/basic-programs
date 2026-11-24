def Largeandsmallnumber(arr): 
    large = arr[0] 
    small = arr[0] 

    for num in arr: 
        if num > large: 
            large = num 
        elif num < small: 
            small = num

    return large, small
a = list(map(int, input().split()))
print(Largeandsmallnumber(a))
