#Peculiar Statistics of the Forward and Reverse Half-Strands
#Re-type this algorithm into the code window below. Then add this function to Replication.py.
#Sample Input:AAAAGGGGA

#Sample Output:

#{0: 4, 1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}


# Input:  Strings Genome and symbol
Genome = "AAAAGGGG"
symbol = "A"
# Output: FasterSymbolArray(Genome, symbol)
def FasterSymbolArray(Genome, symbol):
    array = {}
    n= len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    
    #look at the first half of Genome to compute first array value
    array[0] = PatternCount(symbol, Genome[0:n//2])
    
    for i in range(1, n):
        #start by setting the current array value equal to the previous array value
        array[i] = array[i - 1]
        
        #the current array value can differ from the previous a value by at most 1
        if ExtendedGenome[i - 1] == symbol:
            array[i] = array[i] - 1
        if ExtendedGenome[i + (n//2) - 1] == symbol:
            array[i] = array[i] + 1
    return array
   

# Input:  Strings Text and Pattern
Genome = "AAAAGGGG"
Text = "A"
# Output: The number of times Pattern appears in Text
# HINT:   This code should be identical to when you last implemented PatternCount
def PatternCount(symbol, Genome):
    count = 0 # output variable
    k = len(symbol)
    n = len(Genome)
    for i in range(n - k + 1):
        if symbol[i:i+k] == Genome:
            count += 1
    return Genome.count(symbol)


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
print(FasterSymbolArray(lines[0],lines[1]))