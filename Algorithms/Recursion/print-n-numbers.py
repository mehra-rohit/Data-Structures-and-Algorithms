#print n numbers in descending order

def print_desc(n):
  if n==0:
    return 0
  else: 
    print(n)
    print_desc(n-1)

def print_asc(n):
    # print(n)
    if n==0:
        print(0)
    else: 
        print_asc(n-1)
        print(n)
