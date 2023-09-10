# permutations of a string

def permutations(up,p=''):
    ans = []
    if len(up)==0:
        ans.append(p)
        return ans
    
    ch0 = up[0]
    
    for i in range(len(p)+1):
        s = p[0:i]
        e = p[i:len(p)]
        ans = ans + permutations(up[1:],s+ch0+e)
    return ans

a = permutations('abc')
print(a)

# returns count of permutations
def permutations(up,p=''):
    c = 0
    if len(up)==0:
        c+=1
        return c
    
    ch0 = up[0]
    
    for i in range(len(p)+1):
        s = p[0:i]
        e = p[i:len(p)]
        c += permutations(up[1:],s+ch0+e)
    return c
