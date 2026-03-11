from Bio.Seq import Seq

with open("input.txt", "r") as f:
    lines = f.read().split()
    seq = Seq(lines[0].strip())
    protein = lines[1].strip()

# For each of the tables
for i in [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15]:
    translated = seq.translate(table=i, to_stop=False, stop_symbol="")
    if translated == protein:
        print(i)
        break