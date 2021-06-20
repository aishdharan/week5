import random
import sys

"""
Notes/Questions:
- What happens if bases is a string?
- Try and make seq a string instead of a list of strings
- Otherwise you're on the right track.
"""


def main():
    bases = ['A', 'T', 'G', 'C']
    seq = "".join(random.choices(bases, k=100))
    print("Given sequence =", seq)
    print("Length of sequence =", len(seq))
    for k in range(len(seq)-1):
        k = int(input("Give k_mer: "))
        print("%s %13s" % (f'{k}-mer', 'count'))
        print('-' * 25)
        for value in range(len(seq) - k + 1):
            val_k = seq[value: value + k]
            kmer_count = seq.count(val_k)
            print("%s %13s" % (val_k, kmer_count))
        print("=" * 25)

    # return os.X_OK
    # https://docs.python.org/3/library/os.html#os.X_OK
    # I don't think this is what you want
    return 0  # if running on Windows


if __name__ == "__main__":
    sys.exit(main())