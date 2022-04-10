#m/n - рациональное число
#ввод: m1,n1,m2,n2 (m1/n1 and m2/n2)
#вывод m,n

#sum (m1, n1, m2, n2) --> (m1/n1 + m2/n2)
#sub (m1, n1, m2, n2) --> (m1/n1 - m2/n2)
#mult (m1, n1, m2, n2) --> (m1/n1 * m2/n2)
#div (m1, n1, m2, n2) --> (m1/n1 / m2/n2)

import math

def sum (m1, n1, m2, n2):
    x = m1*n2 + n1*m2
    y = n1*n2
    z = math.gcd(x, y)
    return (x//z, y//z)

def sub (m1, n1, m2, n2):
    m2 = -m2
    return (sum (m1, n1, m2, n2))

def mult (m1, n1, m2, n2):
    m = m1*m2
    n = n1*n2
    k = math.gcd(m,n)
    return (m//k,n//k)


def div (m1, n1, m2, n2):
    m = m1*n2
    n = n1*m2
    k = math.gcd(m,n)
    return (m//k,n//k)