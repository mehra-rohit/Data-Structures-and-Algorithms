#subset of a string
def subset(p, ss, ans = set()):
    if len(ss)==0:
        if len(p)!=0:
            ans.add(p)
        return ans
    ch0 = ss[0]
    return subset(p,ss[1:]).union(subset(ch0+p,ss[1:]))
    
print(subset('','abc'))
