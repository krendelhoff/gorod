from IPython.display import clear_output
from sage.rings.rational import Rational


def kosinp(dim):
    a = [[0 for j in range(0, dim)] for i in range(0, dim)]
    for i in range(0, dim):
        for j in range(i+1, dim):
            print("a["+str(i+1)+"]["+str(j+1)+"] = ")
            a[i][j] = Rational(input())/2
            a[j][i] = -a[i][j]
    return a


def sinp(dim):
    a = [[0 for j in range(0, dim)] for i in range(0, dim)]
    for i in range(0, dim):
        for j in range(i, dim):
            print("a["+str(i+1)+"]["+str(j+1)+"] = ")
            a[i][j] = Rational(input()) if i == j else Rational(input())/2
            a[j][i] = a[i][j]
    return a


def minp(dimr, dimc):
    a = [[0 for j in range(0, dimc)] for i in range(0, dimr)]
    for i in range(0, dimr):
        for j in range(0, dimc):
            print("a["+str(i+1)+"]["+str(j+1)+"] = ")
            a[i][j] = Rational(input())
    return a
