#remove all a's from string
#recursive way
def string_func(string,i=0,ans=''):
    if i==len(string):
        return ans
    if string[i]=='a':
        ans = ''
    else : 
        ans = string[i]
    return ans + string_func(string,i+1)
        

print(string_func('baccadsafasfasfas'))

#with loop
#remove all a's from string
def string_func(string):
    ans = ''
    for i in string:
        if i=='a':
            pass
        else : ans += i
    return ans
        

print(string_func('baccadsafasfasfas'))
