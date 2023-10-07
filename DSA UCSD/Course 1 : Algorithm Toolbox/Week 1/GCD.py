
# Greatest Common Denominator
# largest number d which divides both a and b.
# Integers a,b >0 -----> output d : a/d / b/d

# Naive Approach
# Check for all numbers from 2 to min(a,b)


def gcd_naive(a: int, b: int) -> int:
    gcd_val = 1
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd_val = i
    return gcd_val


# Optimised Approach
# EuclidGCD
# gec(a,b) = gcd(a',b) = gcd(b,a')
# where a' = a%b


def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    a_ = a % b
    return gcd(b, a_)


if __name__ == '__main__':
    assert gcd_naive(10, 5) == 5
    assert gcd_naive(100, 10) == 10
    assert gcd_naive(100000, 10000) == 10000

    assert gcd(10, 5) == 5
    assert gcd(100, 10) == 10
    assert gcd(100000, 10000) == 10000
