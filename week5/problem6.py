import sys

"""
Notes:
- Very good. I've added some remarks below.
"""


def main():
    # fixme: no need to cast to str() because input always returns a string
    sentence = str(input("Enter a sentence: "))
    sent_join = ''.join(sentence).split()
    print(sent_join)
    sent_index = list(enumerate(sent_join))
    # print(sent_index)
    for x, y in sent_index:
        print(f"{x} -> {y}")
    # you can do this; shorter and easier to read
    for index, word in enumerate(sentence.split()):
        print(f"{index} --> {word}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
