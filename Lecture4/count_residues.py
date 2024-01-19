def count_residues(seq):
    freq={}
    seq = seq.lower()
    for res in seq:
        if res in freq:
            freq[res]+=1
        else:
            freq[res]=1
    return freq

freq = count_residues("gatgnnnnnacgaaagxxxxttgt")
for residue in freq.keys():
    print(residue,":", freq[residue])
