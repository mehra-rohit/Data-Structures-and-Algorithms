#remove all a's from string

def string_func(string,i=0,ans=''):
    if i==len(string):
        return ans
    if string[i]=='a':
        ans = ''
    else : 
        ans = string[i]
    return ans + string_func(string,i+1)
        

print(string_func('baccadsafasfasfas'))
