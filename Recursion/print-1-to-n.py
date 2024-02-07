# given integer input n > 0, print 1 to n integer in ascending order

# recursion solution
# hypothesis : print(n) - 1,2,3,......n
# print(n-1) - 1,2,3,......n-1
# call print(n-1) and then print(n)
# base condition : smallest valid input - 1, print(1)

def print_n_asc(n: int) -> None:
    # base condition
    if n == 1:
        print(1)
        return

    print_n_asc(n-1)  # it is important to call func(n-1) first as we want ascending order
    print(n)


def print_n_desc(n: int) -> None:
    # base condition
    if n == 1:
        print(1)
        return
    print(n)
    print_n_desc(n-1)  # it is important to call func(n-1) after printing n as we want descending order


print_n_asc(10)
print_n_desc(10)

