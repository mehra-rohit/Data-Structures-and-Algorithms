
def check_armstring_number(a):
  su = 0 
  temp = a
  while temp >0 :
      rem = temp %10
      su = su + pow(rem,3)
      temp = temp//10
  if su==a:
      print('Armstrong Number')
  else:
      print('Not Armstrong Number')
