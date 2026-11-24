def prime_number(num):
    left = 2
    is_prime = True

    if num <= 1:
        is_prime = False

    else:
        while left < num:
            if num%left == 0:
                is_prime = False

                break
            left+=1

    if is_prime:
        print("prime")
    else:
        print("not primt")


prime = int(input("enter number"))

print(prime_number(prime))