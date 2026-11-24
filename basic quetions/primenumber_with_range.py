def prime_number(start, end):
    left = start
    right = end

    while left <= right:
        if start > 1:
            division = 2
            is_prime = True

            while division < left:
                if left%division == 0:
                    is_prime = False
                    break

                division+=1

            if is_prime:
                print(left, end = "")
        left+=1
s = int(input("enter start number"))
e = int(input("enter end number"))
print(prime_number(s, e))



            


    