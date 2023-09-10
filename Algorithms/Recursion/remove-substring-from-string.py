#remove substring from string

def string_func(string,ss,i=0):
    #base case
    if i==len(string):
        return ''
    
    if string[i:].startswith(ss):
        return string_func(string,ss,i=i+len(ss))
    else : 
        return string[i] + string_func(string,ss,i=i+1)
        
print(string_func('asdadaappleasdasd','apple'))
