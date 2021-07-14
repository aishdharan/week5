import random
import sys

"""
Notes:
- Excellent!
- They can be simplified but at least they now demonstrate to me that you do not what you're writing.
"""


def main():
    l = random.choices(range(0, 101), k=100)
    print(f"l = {l}")
    print(len(l))
    new_l = list()
    j = 0
    # cumulative sum
    for i in l:
        j += i
        new_l.append(j)
    print(f"new_l = {new_l}")

    # adjoin pair sum
    # this is OK; you can still do it without having to create k_list
    new_l1 = []
    k_list = []
    a = len(l) - 1
    print(a)
    for k in range(0, a):
        k_list.append(k)
        new_l1.append(l[k] + l[k + 1])
    print(f"k_list= {k_list}")
    print(f"new_l1 = {new_l1}")

    # sum of three alternate values
    new_l2 = []
    m_list = []  # not very necessary
    b = len(l) - 4
    print(b)
    for m in range(0, b):
        m_list.append(m)
        new_l2.append(l[m] + l[m + 2] + l[m + 4])
    print(f"m_list= {m_list}")
    print(f"new_l2 = {new_l2}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
