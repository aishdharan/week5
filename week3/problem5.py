import os
import sys


def main():
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    d = int(input("d = "))
    e = int(input("e = "))
    f = int(input("f = "))
    g = int(input("g = "))
    h = int(input("h = "))
    i = int(input("i = "))
    j = int(input("j = "))
    k = int(input("k = "))
    l = int(input("l = "))
    m = int(input("m = "))
    n = int(input("n = "))
    o = int(input("o = "))
    p = int(input("p = "))
    q = int(input("q = "))
    r = int(input("r = "))

    list1 = [[a, b, c],
             [d, e, f],
             [g, h, i]]
    print(f'list1 = {list1}')
    list2 = [[j, k, l],
             [m, n, o],
             [p, q, r]]
    print(f'list2 = {list2}')
    s = a * j + b * m + c * p
    t = a * k + b * n + c * q
    u = a * l + b * o + c * r
    v = d * j + e * m + f * p
    w = d * k + e * n + f * q
    x = d * l + e * o + f * r
    y = g * j + h * m + i * p
    z = g * k + h * n + i * q
    _a = g * l + h * o + i * r
    list3 = [[s, t, u],
             [v, w, x],
             [y, z, _a]]
    print(f'list1 x list2 = {list3}')

    return os.X_OK


if __name__ == "__main__":
    sys.exit(main())