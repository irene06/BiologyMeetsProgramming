#Write a function MinimumSkew taking a DNA string Genome as input and returning all integers i minimizing Skew[i] for Genome. Then add this function to Replication.py. (Hint: make sure to call Skew(Genome) as a subroutine, and keep in mind that Python has a built-in min function in addition to max.)
def SkewArray(Genome):
    array = [0]
    Skew = 0
    for i in Genome:
        if i == 'A' or i == 'T':
            Skew += 0
            array.append(Skew)
        if i == 'C':
            Skew -= 1
            array.append(Skew)
        if i == 'G':
            Skew += 1
            array.append(Skew)
    return array

def MinimumSkew(Genome):
    array = SkewArray(Genome)
    positions = []
    count = 0
    minarray = min(array)
    for i in array:
        if i == minarray:
            positions.append(count)
        count +=1
    return positions