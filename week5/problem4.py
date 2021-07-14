import random
import sys

"""
Notes:
- Well done! Much better now.
- The only thing I would strongly suggest is to give some consideration into how you name variables. 
Variable names matter a lot. You don't want them to be too long but you also want them to be 
immediately obvious what they refer to. Avoid ad hoc abbreviations; better have a set of full words 
e.g. 'dna_sequence' than 'dna_seq' which has its own meaning, or better simply 'dna'. Naming is 
an art but perhaps the best way to spend time cleaning up your code. The legibility of Python 
allows you to keep things nice and clean. 
- The main benefit of using git is that commits save snapshot of the repository. Use this to your 
advantage. Always commit the complete state e.g. once it is just barely working do a commit then 
for each improvement do another commit. This will allow you to always have things clean. Once you 
have it working correctly you can then pay attention to variable names for the final commits. 
If you were not working with git then you would have to keep track of all the states of the 
module by commenting things out. No need for this with git. 
"""


def main():
    bases = ['A', 'T', 'G', 'C']
    sequence = random.choices(bases, k=100)
    dna_sequence = ''.join(sequence)
    print(f"DNA sequence = {dna_sequence}")
    rna = dna_sequence.replace("T", "U")
    print(f"RNA sequence = {rna}")
    # todo: which string method can perform transcription for you?
    translated_sequence = []
    # translated_sequence = rna.replace("A", "U").replace("U", "A").replace("C", "G").replace("G", "C")
    for k in rna:
        if k == "A":
            translated_sequence.append("U")
        elif k == "U":
            translated_sequence.append("A")
        elif k == "C":
            translated_sequence.append("G")
        elif k == "G":
            translated_sequence.append("C")

    # print(trans_seq)
    translated_joined = ''.join(translated_sequence)
    print(f"Transcribed sequence = {translated_joined}")
    # print(rna_seq)
    genetic_code = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
                    "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
                    "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
                    "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
                    "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
                    "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
                    "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
                    "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
                    "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
                    "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
                    "UAA": "STOP", "CAA": "Q", "AAA": "K", "GAA": "E",
                    "UAG": "STOP", "CAG": "Q", "AAG": "K", "GAG": "E",
                    "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
                    "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
                    "UGA": "STOP", "CGA": "R", "AGA": "R", "GGA": "G",
                    "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
                    }
    protein = ''
    for i in range(0, len(translated_joined) - (3 + len(translated_joined) % 3), 3):
        if genetic_code[translated_joined[i:i + 3]] == "STOP":
            break
        protein += genetic_code[translated_joined[i:i + 3]]
    print(f"Translated Protein = {protein}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
