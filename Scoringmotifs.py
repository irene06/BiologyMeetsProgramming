# Input:  Motifs, a list of kmers (strings)
# Output: Count(Motifs), the count matrix of Motifs as a dictionary of lists
def Count(Motifs):
    count = {} 
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = [] 
        for j in range(k):
            count[symbol].append(0) 
    t = len(Motifs) 
    for i in range(t): 
        for j in range(k): 
            symbol = Motifs[i][j] 
            
            
            count[symbol][j] += 1
    return count