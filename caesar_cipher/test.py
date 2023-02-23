# from math import ceil
# def how_many_cans():
#     height = float(input("How height is a wall?"))
#     width = float(input("How width is a wall?"))
#     can_area = 6
#     result = (height*width)/can_area
#     result_ceil = ceil(result)
#     return print(f"You need a {round(result, 2)} can of paint, so you need to buy {result_ceil} cans")
#
# how_many_cans()

def is_prime(number):
    is_prime = True
    for n in range(2, number):
        if number % n == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It is not a prime number")


is_prime(17)
