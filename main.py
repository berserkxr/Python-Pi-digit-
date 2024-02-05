from mpmath import *

#setting number of digits
mp.dps = 1000

#setting up pi and the digit of pi you want
pi = str(mp.pi)
dec = int(input('Instert the decimal of pi you want: '))
realdec = dec + 2
pidec = pi[0:realdec]

print(pidec)


