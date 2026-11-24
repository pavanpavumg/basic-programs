


def armstrong_number(num):
    original = num
    temp = num

    digits = 0

    while temp > 0:
        digits+=1
        temp = temp//10


    temp = num
    total = 0

    while temp > 0:
        remider = temp % 10
        total = total + (remider ** digits)
        temp = temp // 10


    if total == original:
        print("yes")
    else:
        print("no")




n = int(input("enter you number"))

print(armstrong_number(n))

    