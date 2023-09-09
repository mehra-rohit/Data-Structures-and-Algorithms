#elucid theorem
# gcd(a,b) = gcd(rem(a,b),a)
# LCM = (a*b)/HCF

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

def lcm(a,b):
    return (a*b)/gcd(a,b)
